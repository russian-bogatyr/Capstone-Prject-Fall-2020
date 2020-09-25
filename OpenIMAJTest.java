package uk.ac.soton.ecs.jsh2;

import org.openimaj.image.ImageUtilities;
import org.openimaj.image.MBFImage;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import org.openimaj.image.DisplayUtilities;

/**
 * OpenIMAJ Hello world!
 *
 */
public class OpenIMAJTest {
    public static void main( String[] args ) throws MalformedURLException, IOException {
    	MBFImage image = ImageUtilities.readMBF(new URL("http://static.openimaj.org/media/tutorial/sinaface.jpg"));
    	System.out.println(image.colourSpace);
        DisplayUtilities.display(image);
    }
}