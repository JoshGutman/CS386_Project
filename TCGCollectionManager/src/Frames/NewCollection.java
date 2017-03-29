package Frames;

import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class NewCollection {

	public NewCollection(){
		// Creates the frame of the Project
		JFrame frame = new JFrame();
		frame.setTitle("Add New Collection");
		frame.setSize(300, 200);
				
		// Creates the logo of the Project
		ImageIcon icon = new ImageIcon("icon.png");
		Image logo = icon.getImage();
		frame.setIconImage(logo);
				
		// Details of the frame
		frame.setResizable(false);
		
		// Adds the buttons
		addButtonsToFrame(frame.getContentPane());
		
		// Starts Frame
        frame.setVisible(true);
	}
	
	public static void addButtonsToFrame(Container pane) {
		// Sets the frame's pane layout
        pane.setLayout(new BoxLayout(pane, BoxLayout.Y_AXIS));
        
        // Creates the forms
        JLabel name = new JLabel("Collection Name: ");
        JTextField nameinput = new JTextField(15);
        name.setFont(new Font("Impact", Font.PLAIN, 16));
        name.setAlignmentX(Component.CENTER_ALIGNMENT);
        nameinput.setAlignmentX(Component.CENTER_ALIGNMENT);
        pane.add(name);
        pane.add(nameinput);
        
        JLabel game = new JLabel("Card Game: ");
        JTextField gameinput = new JTextField(15);
        game.setAlignmentX(Component.CENTER_ALIGNMENT);
        gameinput.setAlignmentX(Component.CENTER_ALIGNMENT);
        game.setFont(new Font("Impact", Font.PLAIN, 16));
        pane.add(game);
        pane.add(gameinput);
        
        // Sets the button dimensions
        Dimension d = new Dimension();
        d.setSize(100, 100);
        
        // Creates the buttons
        JButton add = new JButton("Add");
        add.setAlignmentX(Component.CENTER_ALIGNMENT);
        add.setMaximumSize(d);
        add.setFont(new Font("Impact", Font.PLAIN, 24));
        
        add.addActionListener(new ActionListener(){
        	@Override
        	public void actionPerformed(ActionEvent e) {
        	        // TODO Add Info to Database
        			
        	    }
        });
        
        pane.add(add);
        
        
        
	}
}
