import java.awt.Component;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Image;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class TCGCollectionManager{
	
	public static void main(String[] args){
		new TCGCollectionManager();
	}
	
	public TCGCollectionManager(){
		// Creates the frame of the Project
		JFrame frame = new JFrame();
		frame.setSize(800, 600);
		frame.setTitle("TCGCollectionManager");
		
		// Creates the logo of the Project
		ImageIcon icon = new ImageIcon("icon.png");
		Image logo = icon.getImage();
		frame.setIconImage(logo);
		
		// Details of the frame
		frame.setResizable(false);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		try {
            frame.setContentPane(new JLabel(new ImageIcon(ImageIO.read(new File("bg.jpg")))));
        } catch (IOException e) {
            e.printStackTrace();
        }
		
		addButtonsToFrame(frame.getContentPane());
		
		frame.pack();
        frame.setVisible(true);
	}
	
	public static void addButtonsToFrame(Container pane) {
        pane.setLayout(new BoxLayout(pane, BoxLayout.Y_AXIS));
        
        Dimension d = new Dimension();
        d.setSize(500, 400);
        
        JButton newCol = new JButton("New Collection");
        newCol.setAlignmentX(Component.CENTER_ALIGNMENT);
        newCol.setMaximumSize(d);
        newCol.setFont(new Font("Impact", Font.PLAIN, 40));
        pane.add(newCol);
        
        JButton exCol = new JButton("Existing Collection");
        exCol.setAlignmentX(Component.CENTER_ALIGNMENT);
        exCol.setMaximumSize(d);
        exCol.setFont(new Font("Impact", Font.PLAIN, 40));
        pane.add(exCol);
        
	}
}
