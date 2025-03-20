import java.util.ArrayList;
import java.util.List;

public class Categoria {
    private String nome;
    private List<Produto> produtos;
    private List<Categoria> subcategorias;

    Categoria(String nome){
        this.nome = nome;
        this.produtos = new ArrayList<>();
        this.subcategorias = new ArrayList<>();
    }

    public void adicioneProduto(Produto produto){

        if (!produtos.contains(produto)) {  // Se o produto não está na lista, adiciona
            produtos.add(produto);
            produto.setCategoria(this);     // Atualiza a categoria do produto
        } else {
            // Se o produto já está na lista, podemos garantir que a categoria seja atualizada
            produto.setCategoria(this);
        }

        }

    void adicioneSubcategoria(Categoria subcategoria){
        subcategorias.add(subcategoria);
    }

    String getNome(){
        return nome;
    }

    List<Produto> getProdutos(){
        return produtos;
    }

    List<Categoria> getSubcategorias(){
        return subcategorias;
    }

    void removaSubcategoria(Categoria subcategoria){
        if (!subcategorias.contains(subcategoria)) {
            throw new IllegalArgumentException("Essa subcategoria não existe!");
        }
    
        if (permanente) {
            // Move produtos da subcategoria para esta categoria
            for (Produto produto : subcategoria.getProdutos()) {
                produto.setCategoria(this);  // Reatribui a categoria
                produtos.add(produto);       // Adiciona o produto a esta categoria
            }
    
            // Move subcategorias da subcategoria removida para esta categoria
            for (Categoria subSubcategoria : subcategoria.getSubcategorias()) {
                subcategorias.add(subSubcategoria);
            }
        }
    
        // Remove a subcategoria após a operação
        subcategorias.remove(subcategoria);
    }

}
