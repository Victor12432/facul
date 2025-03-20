public class CartaoCreditoStrategy implements PagamentoStrategy {
    private String numeroCartao;
    private String nomeTitular;
    private String cvv;
    private String validade;

    public CartaoCreditoStrategy(String numeroCartao, String nomeTitular, String cvv, String validade) {
        this.numeroCartao = numeroCartao;
        this.nomeTitular = nomeTitular;
        this.cvv = cvv;
        this.validade = validade;
    }

    @Override
    public void pagar(double valor) {
        System.out.println("Pagamento de R$" + valor + " realizado com cartão de crédito.");
    }
}
