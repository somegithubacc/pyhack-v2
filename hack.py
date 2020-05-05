import pymem, time, c_process, offsets, c_features, config

def main( ):
    process = c_process.c_process( )
    print( f"client_panorama address { process.client_panorama.lpBaseOfDll }" )
    offsets.client_panorama = process.client_panorama.lpBaseOfDll
    print( f"engine address { process.engine.lpBaseOfDll }" )
    offsets.engine = process.engine.lpBaseOfDll
    cooldown = input( "Cooldown Time (ms): " )
    config.force_radar = input( "Force Radar: " )
    config.no_flash = input( "No Flash: " )
    config.glow = input( "Glow: " )
    config.auto_bunnyhop = input( "Auto Bunnyhop: " )

    glow_mode = input( "Glow Mode, 0 For Preset, Anything Else For Custom:" )

    if int( glow_mode ) != 0:
        config.glow_color[ 0 ] = input( "Glow R (float): " )
        config.glow_color[ 1 ] = input( "Glow G (float): " )
        config.glow_color[ 2 ] = input( "Glow B (float): " )
        config.glow_color[ 3 ] = input( "Glow A (float): " )

    features = c_features.c_features( process.process )

    while True:
        if features.local_player:
            features.run( )

        time.sleep( int( cooldown ) / 1000 )
    
main( )