package DS2;

public class Item {
    private String nome;
    private double preco;

    public void Item(String nome, double preco){
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }
    public double getPreco() {
        return preco;
    }
}
