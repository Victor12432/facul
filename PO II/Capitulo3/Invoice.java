package Capitulo3;
/**
 * Invoice
 */
public class Invoice {

    private String numero;
    private String descricao;
    private int quantidade;
    private double preco;


    public void setNumero(String numero){
        this.numero = numero;
    }
    public String getNumero(){
        return numero;
    }
    
    public void setDescricao(String descricao){
        this.descricao = descricao;
    }
    public String getDescricao(){
        return descricao;
    }
    
    public void setQuantidade(int quantidade){
        this.quantidade = quantidade;
    }
    public int getQuantidade(){
        return quantidade;
    }
    
    public void setPreco(double preco){
        this.preco = preco;
    }
    public double getPreco(){
        return preco;
    }

    /**
     * @param preco
     * @param quantidade
     * @return
     */
    public double getInvoiceAmount(double preco, int quantidade){
        if (quantidade < 0){
            quantidade = 0; 
        }
        if(preco < 0){
            preco = 0.0;
        }
        return preco*quantidade;
    }
}