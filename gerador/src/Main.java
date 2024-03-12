import static java.lang.System.out;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        // Exemplo de uso para Cliente
        Cliente cliente = Cliente.gerarClienteAleatorio();
        ClienteDao clienteDao = new ClienteDao();
        clienteDao.salvarCliente(cliente);
        Cliente clienteRecuperado = clienteDao.buscarCliente(cliente.getId());

        // Exemplo de uso para Funcionario
        Funcionario funcionario = Funcionario.gerarFuncionarioAleatorio();
        FuncionarioDao funcionarioDao = new FuncionarioDao();
        funcionarioDao.salvarFuncionario(funcionario);
        Funcionario funcionarioRecuperado = funcionarioDao.buscarFuncionario(funcionario.getId());

        // Exemplo de uso para Venda
        Venda venda = Venda.gerarVendaAleatoria();
        VendaDao vendaDao = new VendaDao();
        vendaDao.salvarVenda(venda);
        Venda vendaRecuperada = vendaDao.buscarVenda(venda.getId());
    }
}




