package Frames;
import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.BorderLayout;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.ScrollPaneLayout;
import javax.swing.SwingUtilities;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// TODO
// - Add ability to remove collections
// - Add ability to add cards to collections
// - Add ability to view added cards

public class CollectionSelect {
	
	public static JPanel buttonPanel = new JPanel();
	public static JPanel titlePanel = new JPanel();
	public static JPanel collectionButtons = new JPanel();
	public static JPanel mainPanel = new JPanel();
	public static JScrollPane collections = new JScrollPane();
	
	public CollectionSelect() {
		
		
		// Creates the frame of the Project
		JFrame frame = new JFrame();
		frame.setTitle("TCG Manager");
		
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
		
		buttonPanel = new JPanel();
		titlePanel = new JPanel();
		collectionButtons = new JPanel();
		mainPanel = new JPanel();
		collections = new JScrollPane();
		
		ArrayList<Collection> collectionList = new ArrayList<Collection>();
		
		// Set layout managers for each panel
		buttonPanel.setLayout(new FlowLayout(FlowLayout.RIGHT));
		titlePanel.setLayout(new BorderLayout());
		collectionButtons.setLayout(new BoxLayout(collectionButtons, BoxLayout.Y_AXIS));
		mainPanel.setLayout(new BorderLayout());
		pane.setLayout(new BorderLayout());
		
		
		// Get existing collections from 'collections.txt'
		try {
			ObjectInputStream log = new ObjectInputStream(new FileInputStream("collections.txt"));
			Object obj = log.readObject();
			try {
				while (obj != null) {
					collectionList.add((Collection)obj);
					obj = log.readObject();
				}
			} catch (EOFException e){
				
			}
			log.close();
		} catch (FileNotFoundException e1) {
			//e1.printStackTrace();
		} catch (IOException e2) {
			e2.printStackTrace();
		} catch (ClassNotFoundException e3) {
			e3.printStackTrace();
		}
		
		
		
        // Sets the button dimensions
        Dimension d = new Dimension();
        d.setSize(1020, 50);
        
        // Creates the buttons
        JButton newCol = new JButton("New Collection");
        newCol.setAlignmentX(Component.CENTER_ALIGNMENT);
        newCol.setMaximumSize(d);
        newCol.setFont(new Font("Impact", Font.PLAIN, 20));
        
        newCol.addActionListener(new ActionListener(){
        	@Override
        	public void actionPerformed(ActionEvent e) {
        	        new NewCollection(); 
        	        SwingUtilities.updateComponentTreeUI(mainPanel);
        	    }
        });
        
        
        // Create buttons for every existing collection
        for (Collection c : collectionList){
        	JButton temp = new JButton(c.getName());
        	temp.setAlignmentX(Component.LEFT_ALIGNMENT);
            temp.setMaximumSize(d);
            temp.setFont(new Font("Impact", Font.PLAIN, 20));
            collectionButtons.add(temp);
        }
        // Add collections to JScrollPane
        collections.setVisible(true);
        collections.add(collectionButtons);
        collections.setViewportView(collectionButtons);
               
        JLabel title = new JLabel("TCG Manager");
        title.setFont(new Font("Impact", Font.PLAIN, 20));
        title.setHorizontalAlignment(JLabel.CENTER);
               
        buttonPanel.add(newCol);
        titlePanel.add(title, BorderLayout.CENTER);
        titlePanel.add(buttonPanel, BorderLayout.EAST);
        mainPanel.add(titlePanel, BorderLayout.NORTH);
        mainPanel.add(collections, BorderLayout.CENTER);
        pane.add(mainPanel, BorderLayout.CENTER);
        
	}
	
	// Refresh window when a new Collection is added
	public static void refreshWindow() {
		ArrayList<Collection> collectionList = new ArrayList<Collection>();
		
		// Get existing collections from 'collections.txt'
		try {
			ObjectInputStream log = new ObjectInputStream(new FileInputStream("collections.txt"));
			Object obj = log.readObject();
			try {
				while (obj != null) {
					collectionList.add((Collection)obj);
					obj = log.readObject();
				}
			} catch (EOFException e){
				
			}
			log.close();
		} catch (FileNotFoundException e1) {
			//e1.printStackTrace();
		} catch (IOException e2) {
			e2.printStackTrace();
		} catch (ClassNotFoundException e3) {
			e3.printStackTrace();
		}
		
		collectionButtons = new JPanel();
		
		// Create buttons for every existing collection
        for (Collection c : collectionList){
        	JButton temp = new JButton(c.getName());
        	temp.setAlignmentX(Component.LEFT_ALIGNMENT);
            temp.setMaximumSize(new Dimension(1020, 50));
            temp.setFont(new Font("Impact", Font.PLAIN, 20));
            collectionButtons.add(temp);
        }
		
		
        collections.setVisible(true);
        collections.add(collectionButtons);
        collections.setViewportView(collectionButtons);
               
        JLabel title = new JLabel("TCG Manager");
        title.setFont(new Font("Impact", Font.PLAIN, 20));
        title.setHorizontalAlignment(JLabel.CENTER);
               
        titlePanel.add(title, BorderLayout.CENTER);
        titlePanel.add(buttonPanel, BorderLayout.EAST);
        mainPanel.add(titlePanel, BorderLayout.NORTH);
        mainPanel.add(collections, BorderLayout.CENTER);
        
		mainPanel.invalidate();
		mainPanel.validate();
	}
}
