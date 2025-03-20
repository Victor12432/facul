public class ItemCompra {
    private Produto produto;
    private int quantidade;
    private Vendedor vendedor;

    public ItemCompra(Produto produto, int quantidade, Vendedor vendedor ){
        if (produto != null){
            this.produto = produto;
        }else{
            throw new IllegalArgumentException("Nenhum produto foi especificado");
        }
        if (vendedor != null){
            this.vendedor = vendedor;
        }else{
            throw new IllegalArgumentException("Nenhum vendedor foi especificado");
        }
        if (quantidade > 0){
            this.quantidade = quantidade;
        }else{
            throw new IllegalArgumentException("A quantidade deve ser pelo menos um valor maior que 0");
        } 
    }
    

    public Vendedor getVendedor() {
        return vendedor;
    }

    private void setVendedor(Vendedor vendedor) {
        this.vendedor = vendedor;
    }

    public int getQuantidade() {
        return quantidade;
    }

    private void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public Produto getProduto() {
        return produto;
    }

    public Produto getNomeProduto() {
        return produto;
    }

    private void setProduto(Produto produto) {
        this.produto = produto;
    }


}
