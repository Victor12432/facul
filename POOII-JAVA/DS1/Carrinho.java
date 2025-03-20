import java.util.List;
import java.util.ArrayList;

public class Carrinho {
    private List<ItemCompra> itens;

    public Carrinho() {
        this.itens = new ArrayList<>();
    }

    public void adicioneItem(Produto produto,Vendedor vendedor, int quantidade){
        int QuantidadeDisponivel = vendedor.getEstoque().quantidadeEmEstoque(produto); // pega a quantidade que o vendedor tem do item
        if(QuantidadeDisponivel >= quantidade){ // vê se o vendedor tem a quantidade requisitada
          for(ItemCompra item : itens ){ // vê se tem o produto no carrinho
              if(item.getProduto().equals(produto)){// vê se tem o produto no carrinho(list<itemcompra> itens) <- esse é o carrinho
                 if(quantidade + item.getQuantidade() <= QuantidadeDisponivel){ // se a quantidade a se adicionar + a quantide que já tem está disponivel
                     item.setQuantidade(quantidade + item.getQuantidade());// seta essa nova quantidade
                     return; // sai do método
                 } else { 
                 throw new IllegalArgumentException("a quantidade total (já existente no carrinho mais a nova) ultrapassou a quantidade em estoque");
                       }
                 }

            }
             ItemCompra adicionar = new ItemCompra(produto,quantidade,vendedor);
             System.out.println( produto.getNome() + " foi adicionado ao carrinho de " + vendedor.getNome()+ "em " + quantidade + " unidades" );
             itens.add(adicionar);
        } else {throw new IllegalArgumentException("quantidade solicitada excedeu a quantidade disponível em estoque");}
    }

    public List<ItemCompra> getItens() {
        return itens;
    }
    
    public void removaItem(Produto produto) {
        itens.removeIf(item -> item.getProduto().equals(produto));
    }

}
