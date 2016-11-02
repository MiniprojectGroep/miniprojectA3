from PIL import Image

def main( ): #{
    filename = "welcome.jpg"
    image = Image.open( filename );
    size =  width, height = image.size;
    image.resize( ( 1200, 100) ).show();
    del image;
#}

if ( __name__ == "__main__" ): #{
    main();
#}
