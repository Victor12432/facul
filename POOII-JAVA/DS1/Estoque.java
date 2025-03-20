import java.util.List;
import java.util.ArrayList;

public class Estoque {
    private List<ItemEstoque> itens;

    public Estoque(){
        this.itens = new ArrayList<>();
    }
    
    public void adicioneItem(Produto produto, int quantidade) {
        for (ItemEstoque item : itens) {
            if (item.getProduto().equals(produto)) {
                item.adicioneQuantidade(quantidade);
                return;
            }
        }
        itens.add(new ItemEstoque(produto, quantidade));
    }
    public List<ItemEstoque> getItens() {
        return itens;
    }

    public int quantidadeEmEstoque(Produto produto){
        for (ItemEstoque item : itens) {
            if (item.getProduto().equals(produto)) {
                return item.getQuantidade();
            }
        }
        return 0; // Produto não encontrado
    }
    

    public void reduzaQuantidade(Produto produto, int quantidade)  throws IllegalArgumentException {
        for (ItemEstoque item : itens) {
            if (item.getProduto().equals(produto)) {
                int quantidadeAtual = item.getQuantidade();
    
                if (quantidade > quantidadeAtual) {
                    throw new IllegalArgumentException("Quantidade solicitada maior que a disponível.");
                } else if (quantidade == quantidadeAtual) {
                    itens.remove(item); // Remove o item quando a quantidade chega a 0
                } else {
                    item.setQuantidade(quantidadeAtual - quantidade); // Reduz a quantidade
                }
                return; // Sai após encontrar e processar o produto
            }
        }
        throw new IllegalArgumentException("Produto não encontrado no estoque."); // Se o produto não foi encontrado
    }

}
