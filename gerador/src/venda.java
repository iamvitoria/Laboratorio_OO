import java.util.Random;

// Classe para representar uma Venda
class Venda {
    private int id;
    private int clienteId;
    private int funcionarioId;
    private double valor;

    // getters e setters
    // ...

    // Método para gerar dados aleatórios para uma Venda
    public static Venda gerarVendaAleatoria() {
        Random random = new Random();
        Venda venda = new Venda();
        venda.setId(random.nextInt(1000));
        venda.setClienteId(random.nextInt(1000));
        venda.setFuncionarioId(random.nextInt(1000));
        venda.setValor(random.nextDouble() * 1000);
        return venda;
    }

    private void setId(int i) {

    }

    private void setValor(double v) {

    }

    private void setFuncionarioId(int i) {

    }

    private void setClienteId(int i) {

    }

    public int getId() {
        return 0;
    }
}