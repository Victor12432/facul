public class Pessoa {
    private String nome;

    Pessoa(){};

    public Pessoa(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        if(!nome.isEmpty()){
            this.nome = nome;
        }
    }
}
