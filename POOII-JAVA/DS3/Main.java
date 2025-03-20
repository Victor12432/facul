/**
 UFSC/CTC/INE/INE5404
 Description:

 @author Professor Cancian
 @version
 @since
 */
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

/**
 Programa principal para testar leitura e escrita de produtos.
 */
public class Main {
	public static void main(String[] args) {
	    // Para o teste de persistência apenas da classe Produto em arquivo texto
		try {
			String filePath = "produtos.txt";

			// Criação de instâncias de Produto
			Produto p1 = new Produto("Smartphone", "Galaxy S21", "Samsung", 5000.0, "Eletrônicos");
			Produto p2 = new Produto("Notebook", "XPS 13", "Dell", 9000.0, "Informática");
			Produto p3 = new Produto("Smartwatch", "Apple Watch", "Apple", 3000.0, "Acessórios");

			List<Produto> produtosOriginais = Arrays.asList(p1, p2, p3);

			// Salvar os produtos no arquivo
			Produto.salvarProdutos(produtosOriginais, filePath);
			System.out.println("Produtos salvos no arquivo: " + filePath);

			// Carregar os produtos do arquivo
			List<Produto> produtosCarregados = Produto.carregarProdutos(filePath);
			System.out.println("Produtos carregados do arquivo:");
			for (Produto p : produtosCarregados) {
				System.out.println(p);
			}

			// Comparar produtos originais com os carregados
			boolean iguais = produtosOriginais.equals(produtosCarregados);
			System.out.println("Os produtos carregados são iguais aos originais? " + (iguais ? "Sim" : "Não"));

		} catch (IOException | IllegalArgumentException e) {
			e.printStackTrace();
		}

	    // Para o teste de persistência das classes Categoria e Produto, hierarquicamente, em arquivo texto
		try {
			String fileName = "categoria_hierarquia.txt";

			// Criação da hierarquia de categorias e produtos
			Categoria raiz = new Categoria("Raiz");
			Categoria sub1 = new Categoria("Subcategoria 1");
			Categoria sub2 = new Categoria("Subcategoria 2");
			Categoria sub1_1 = new Categoria("Subcategoria 1.1");
			Categoria sub1_2 = new Categoria("Subcategoria 1.2");
			Categoria sub2_1 = new Categoria("Subcategoria 2.1");
			Categoria sub2_2 = new Categoria("Subcategoria 2.2");

			// Adicionando subcategorias
			sub1.adicionarSubcategoria(sub1_1);
			sub1.adicionarSubcategoria(sub1_2);
			sub2.adicionarSubcategoria(sub2_1);
			sub2.adicionarSubcategoria(sub2_2);
			raiz.adicionarSubcategoria(sub1);
			raiz.adicionarSubcategoria(sub2);

			// Adicionando produtos às categorias
			adicionarProdutos(raiz, "Produto Raiz");
			adicionarProdutos(sub1, "Produto Sub1");
			adicionarProdutos(sub2, "Produto Sub2");
			adicionarProdutos(sub1_1, "Produto Sub1_1");
			adicionarProdutos(sub1_2, "Produto Sub1_2");
			adicionarProdutos(sub2_1, "Produto Sub2_1");
			adicionarProdutos(sub2_2, "Produto Sub2_2");

			// Salvar a categoria raiz
			Categoria.salvarCategoria(raiz, fileName);
			System.out.println("Categoria raiz salva com sucesso!");

			// Carregar a categoria raiz
			Categoria carregada = Categoria.carregarCategoria(fileName);
			System.out.println("Categoria carregada: " + carregada);

			// Comparação
			System.out.println("Categorias iguais? " + raiz.equals(carregada));

		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}

	/**
	 Adiciona 3 produtos a uma categoria.

	 @param categoria A categoria à qual os produtos serão adicionados.
	 @param nomeBase  O nome base para os produtos.
	 */
	private static void adicionarProdutos(Categoria categoria, String nomeBase) {
		for (int i = 1; i <= 3; i++) {
			Produto produto = new Produto(
					nomeBase + " " + i,
					"Modelo " + nomeBase + " " + i,
					"Marca " + nomeBase + " " + i,
					i * 100.0,
					categoria.getNome()
			);
			categoria.adicionarProduto(produto);
		}
	}
}
