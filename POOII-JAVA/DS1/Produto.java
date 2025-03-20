public class Produto {
    private String nome;
    private String modelo;
    private String marca;
    private Double preco;
    private Categoria categoria;

    public Produto(String nome, String modelo, String marca, Double preco, Categoria categoria){
        setNome(nome);
        setCategoria(categoria);
        setMarca(marca);
        setModelo(modelo);
        setPreco(preco);
    }

    public String getNome() {
        return nome;
    }

    private void setNome(String nome) {
        this.nome = nome;
    }

    public String getModelo() {
        return modelo;
    }

    private void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    private void setMarca(String marca) {
        this.marca = marca;
    }

    public Double getPreco() {
        return preco;
    }

    private void setPreco(Double preco) {
        this.preco = preco;
    }

    public Categoria getCategoria() {
        return categoria;
    }

    private void setCategoria(Categoria categoria) {
        this.categoria = categoria;
    }


}
