import java.util.Random;


// Classe para representar um Cliente
class Cliente {
    private int id;
    private String nome;
    private String endereco;

    // getters e setters
    // ...

    // Método para gerar dados aleatórios para um Cliente
    public static Cliente gerarClienteAleatorio() {
        Random random = new Random();
        Cliente cliente = new Cliente();
        cliente.setId(random.nextInt(1000));
        cliente.setEndereco("Endereco" + cliente.getId());
        return cliente;
    }

    private void setEndereco(String s) {
    }

    int getId() {
        return -1; // ou 0, ou outro valor padrão
    }


    private void setId(int i) {

    }
}
