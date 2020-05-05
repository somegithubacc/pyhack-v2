import pymem, offsets, config, utilities, keyboard

class c_features( ):
    def __init__( self, process ):
        self.process = process
        self.local_player = self.process.read_int( offsets.client_panorama + offsets.local_player )

    def force_radar( self, entity ):
        self.process.write_int( entity + offsets.spotted, 1 )

    def no_flash( self ):
        flash_duration = self.process.read_int( self.local_player + offsets.flash_duration )

        if flash_duration > 0.0:
            self.process.write_float( self.local_player + offsets.flash_duration, 0.0 )

    def glow( self, entity ):
        glow_index = self.process.read_int( entity + offsets.glow_index )

        glow_object_manager = self.process.read_int( offsets.client_panorama + offsets.glow_object_manager )

        glow_ptr = glow_object_manager + glow_index * 0x38

        self.process.write_int( glow_ptr + offsets.glow_object_render_while_occluded, 1 )

        utilities.write_color( self.process.process_handle, glow_ptr + offsets.glow_object_color, config.glow_color )

    def auto_bunnyhop( self ):
        if not keyboard.is_pressed( "space" ):
            return

        flags = self.process.read_int( self.local_player + offsets.flags )

        if flags & ( 1<<0 ):
            self.process.write_int( offsets.client_panorama + offsets.force_jump, 5 )
        else:
            self.process.write_int( offsets.client_panorama + offsets.force_jump, 4 )

    def run( self ):
        local_player_team = self.process.read_int( self.local_player + offsets.team_num )

        for i in range( 0, 64 ):
            entity = self.process.read_int( offsets.client_panorama + offsets.entity_list + i * 0x10 )

            if entity:
                health = self.process.read_int( entity + offsets.health )
                team = self.process.read_int( entity + offsets.team_num )
                dormant = self.process.read_int( entity + offsets.dormant )

                if health > 0 and not dormant:
                    
                    if team != local_player_team:

                        if config.force_radar != "0":
                            self.force_radar( entity )

                        if config.glow != "0":
                            self.glow( entity )

        if config.no_flash != "0":
            self.no_flash( )

        if config.auto_bunnyhop != "0":
            self.auto_bunnyhop( )