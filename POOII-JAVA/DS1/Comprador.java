import java.util.ArrayList;
import java.util.List;

public class Comprador extends Pessoa {

    private Carrinho carrinho;

    public Comprador(String nome){
        this.nome = nome;
        carrinho = new Carrinho();
    }

    public void adicioneAoCarrinho(Produto produto, Vendedor vendedor, int quantidade){
        carrinho.adicioneItem(produto,vendedor,quantidade);
    }

    public void efetuarCompra(){
        List<ItemCompra> itensParaRemover = new ArrayList<>();

        for (ItemCompra item : carrinho.getItens()) {
            Produto produto = item.getProduto();
            Vendedor vendedor = item.getVendedor();
            int quantidadeDesejada = item.getQuantidade();

            try {
                vendedor.getEstoque().reduzaQuantidade(produto, quantidadeDesejada);
                item.setQuantidade(0);
                itensParaRemover.add(item);
            } catch (IllegalArgumentException e) {
            }
        }

        carrinho.getItens().removeAll(itensParaRemover);
        formaPagamento(produto, quantidade);
    }

    public void formaPagamento(Produto produto, int quantidade){
        
    }
    public Carrinho getCarrinho(){
        return carrinho;
    }
}
