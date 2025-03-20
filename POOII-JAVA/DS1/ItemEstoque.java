public class ItemEstoque {
    Produto produto;
    int quantidade;

    ItemEstoque(Produto produto, int quantidade) {
        setProduto(produto);
        setQuantidade(quantidade);
    }


    public int getQuantidade() {
        return quantidade;
    }

    void adicioneQuantidade(int quantidade){
        int atual = getQuantidade();
        setQuantidade(atual + quantidade);
    }

    void removaQuantidade(int quantidade){
        int atual = getQuantidade();
        setQuantidade(atual - quantidade);
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public Produto getProduto() {
        return produto;
    }

    private void setProduto(Produto produto) {
        this.produto = produto;
    }




}
