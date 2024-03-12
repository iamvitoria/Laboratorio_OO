import java.util.Random;

// Classe para representar um Funcionario
class Funcionario {
    private int id;
    private String nome;
    private String cargo;

    // getters e setters
    // ...

    // Método para gerar dados aleatórios para um Funcionario
    public static Funcionario gerarFuncionarioAleatorio() {
        Random random = new Random();
        Funcionario funcionario = new Funcionario();
        funcionario.setId(random.nextInt(1000));
        funcionario.setCargo("Cargo" + funcionario.getId());
        return funcionario;
    }

    private void setCargo(String s) {
    }

    int getId() {
        return -1; // ou 0, ou outro valor padrão
    }


    private void setId(int i) {

    }
}
