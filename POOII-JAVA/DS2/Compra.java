public class Compra {
    private double valor;
    private PagamentoStrategy estrategiaPagamento;

    public Compra(double valor) {
        this.valor = valor;
    }

    // Define a estratégia de pagamento
    public void setEstrategiaPagamento(PagamentoStrategy estrategiaPagamento) {
        this.estrategiaPagamento = estrategiaPagamento;
    }

    // Realiza o pagamento usando a estratégia atual
    public void realizarPagamento() {
        if (estrategiaPagamento != null) {
            estrategiaPagamento.pagar(valor);
        } else {
            System.out.println("Estratégia de pagamento não definida.");
        }
    }
}
