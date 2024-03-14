import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GeradorInterface {

    private JFrame frame;
    private JPanel panel;
    private JTextField caminhoInput;
    private JButton gerarButton;

    public GeradorInterface() {
        frame = new JFrame("Gerador de Classes");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        panel = new JPanel();
        panel.setLayout(new GridLayout(2, 2));

        JLabel caminhoLabel = new JLabel("Caminho para a base de dados:");
        caminhoInput = new JTextField();
        caminhoInput.setPreferredSize(new Dimension(200, 20));

        gerarButton = new JButton("Gerar Classes");
        gerarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String caminho = caminhoInput.getText();
                gerarClasses(caminho);
            }
        });

        panel.add(caminhoLabel);
        panel.add(caminhoInput);
        panel.add(gerarButton);

        frame.getContentPane().add(panel);
        frame.pack();
        frame.setVisible(true);
    }

    private void gerarClasses(String caminho) {
        // Implemente a lógica para gerar as classes com o caminho fornecido
        // Isso pode envolver a leitura dos metadados da base de dados e a geração das classes correspondentes
        System.out.println("Gerando classes com o caminho: " + caminho);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new GeradorInterface();
            }
        });
    }
}
