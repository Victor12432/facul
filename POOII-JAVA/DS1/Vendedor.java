public class Vendedor extends Pessoa {
    private Estoque estoque;
    public Vendedor(String nome){
        setNome(nome);
        estoque = new Estoque();
    }

    public void adicioneProdutoAoEstoque(Produto produto, int quantidade){
        estoque.adicioneItem(produto, quantidade);
    }

    public Estoque getEstoque(){
        return estoque;
    }
}
