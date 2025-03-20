import java.util.List;
import java.util.ArrayList;

public class Mercado {
    private List<Categoria> categorias;
    private List<Comprador> compradores;
    private List<Vendedor> vendedores;
    
    public Mercado(){
        this.categorias = new ArrayList<>();
        this.compradores = new ArrayList<>();
        this.vendedores = new ArrayList<>();
    }

    void adicioneCategoria(Categoria categoria){
        if(!categorias.contains(categoria))
            categorias.add(categoria);
    }

    void adicioneComprador(Comprador comprador){
        if(!compradores.contains(comprador))
            compradores.add(comprador);
    }

    void adicioneVendedor(Vendedor vendedor){
        if(!vendedores.contains(vendedor))
            vendedores.add(vendedor);
    }

    public List<Vendedor> getVendedores() {
        return vendedores;
    }

    public List<Comprador> getCompradores() {
        return compradores;
    }

    public List<Categoria> getCategorias() {
        return categorias;
    }

}
