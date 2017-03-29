package Frames;
import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class CollectionSelect {
	
	public CollectionSelect(){
		// Creates the frame of the Project
		JFrame frame = new JFrame();
		frame.setTitle("Collection Select");
		
		// Creates the logo of the Project
		ImageIcon icon = new ImageIcon("icon.png");
		Image logo = icon.getImage();
		frame.setIconImage(logo);
		
		// Details of the frame
		frame.setResizable(false);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// Sets the Background of the program
		try {
            frame.setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("bg.jpg")))));
        } catch (IOException e) {
            e.printStackTrace();
        }
		
		// Adds the buttons
		addButtonsToFrame(frame.getContentPane());
		
		// Starts Frame
		frame.pack();
        frame.setVisible(true);
	}
	
	public static void addButtonsToFrame(Container pane) {
		// Sets the frame's pane layout
        pane.setLayout(new BoxLayout(pane, BoxLayout.Y_AXIS));
        
        // Sets the button dimensions
        Dimension d = new Dimension();
        d.setSize(500, 400);
        
        // Creates the buttons
        JButton newCol = new JButton("New Collection");
        newCol.setAlignmentX(Component.CENTER_ALIGNMENT);
        newCol.setMaximumSize(d);
        newCol.setFont(new Font("Impact", Font.PLAIN, 40));
        
        newCol.addActionListener(new ActionListener(){
        	@Override
        	public void actionPerformed(ActionEvent e) {
        	        new NewCollection();
        	    }
        });
        pane.add(newCol);
        
        JButton exCol = new JButton("Existing Collection");
        exCol.setAlignmentX(Component.CENTER_ALIGNMENT);
        exCol.setMaximumSize(d);
        exCol.setFont(new Font("Impact", Font.PLAIN, 40));
        exCol.addActionListener(new ActionListener(){
        	@Override
        	public void actionPerformed(ActionEvent e) {
        	        new ExCollection();
        	    }
        });
        pane.add(exCol);
        
	}
}
