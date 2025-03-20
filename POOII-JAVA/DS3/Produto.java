/**
 UFSC/CTC/INE/INE5404
 Description:

 @author Professor Cancian
 @version
 @since
 */
import java.io.*;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 Classe Produto representa um item com nome, modelo, marca, preço e categoria.
 Permite persistir e recuperar objetos de produtos em arquivos texto.
 */
public class Produto {

	/**
	 Cria uma instância de Produto a partir de uma string formatada no estilo CSV.
	 A string deve conter o nome da classe em maiusculas ("PRODUTO") e os atributos do produto separados por ponto e vírgula,
	 na ordem:
	 PRODUTO;nome;modelo;marca;preco;nomeCategoria.

	 @param linha Uma string contendo os atributos do produto separados por ponto e vírgula.

	 @return Uma nova instância de Produto com os atributos lidos.

	 @throws IllegalArgumentException Se o formato da string for inválido ou não contiver
	                                  os valores esperados.

	 <p>
	 Este método é usado para reconstruir um objeto Produto a partir de um registro
	 salvo em um arquivo texto. A string deve estar no formato:
	 <pre>
	 PRODUTO;nome;modelo;marca;preco;nomeCategoria
	 </pre>
	 Durante a leitura:
	 <ul>
	 <li>O método divide a string em partes usando ponto e vírgula como delimitador,
	 por meio do método {@link String#split}.</li>
	 <li>Verifica se o número correto de partes foi fornecido (6).</li>
	 <li>Converte o valor de preço de string para um número decimal usando
	 {@link Double#parseDouble}.</li>
	 <li>Cada parte é então atribuída ao atributo correspondente da instância.</li>
	 </ul>
	 Caso o formato esteja incorreto (menos ou mais campos, valores inválidos), o
	 método lança uma exceção {@link IllegalArgumentException}.
	 </p>
	 */
	public static Produto carregarProduto(String linha) {
		String[] campos = linha.split(";");
		if (campos.length != 6) {
			throw new IllegalArgumentException("Linha inválida: " + linha);
		}
		assert campos[1].trim().equals("PRODUTO");
		return new Produto(
				campos[1].trim(),
				campos[2].trim(),
				campos[3].trim(),
				Double.parseDouble(campos[4].trim()),
				campos[5].trim()
		);
	}

	/**
	 Carrega uma lista de produtos de um arquivo texto.
	 <p>
	 Este método pode utilizar a classe {@link BufferedReader} ou a classe {@link Scanner} (ou outras),
	 que permitem leituras eficientes de arquivos texto linha por linha, e a classe {@link Files} para manipulação de arquivos.
	 <p>
	 A leitura deve ser compatível com o formato definido em {@link salvarProdutos}.
	 Cada linha no arquivo representa um produto, com o nome "PRODUTO" e seus atributos separados por ponto e vírgula (`;`).
	 O formato esperado para cada linha deve ser:
	 <pre>
	 PRODUTO;nome;modelo;marca;preco;nomeCategoria
	 </pre>
	 <p>
	 O método deve ler cada linha do arquivo, dividir os atributos com base no separador `;` (usando o metodo split de String)
	 e deve criar uma instância da classe Produto para cada linha.

	 @param filePath Caminho completo do arquivo de onde os produtos serão carregados.

	 @return Lista de objetos Produto carregados do arquivo.

	 @throws IOException              Caso ocorra um erro de leitura no arquivo.
	 @throws IllegalArgumentException Caso o formato da linha no arquivo seja inválido.
	 */
	public static List<Produto> carregarProdutos(String filePath) throws IOException {
		List<Produto> produtos = new ArrayList<>();
		try (BufferedReader reader = Files.newBufferedReader(Paths.get(filePath))) {
			String linha;
			while ((linha = reader.readLine()) != null) {
				// Divide os valores da linha usando ponto e vírgula
				String[] campos = linha.split(";");
				if (campos.length != 6) {
					throw new IllegalArgumentException("Linha inválida: " + linha);
				}
				// Extrai os atributos e cria uma nova instância de Produto
				assert campos[0].trim().equals("PRODUTO");
				String nome = campos[1].trim();
				String modelo = campos[2].trim();
				String marca = campos[3].trim();
				double preco;
				try {
					preco = Double.parseDouble(campos[4].trim());
				} catch (NumberFormatException e) {
					throw new IllegalArgumentException("Preço inválido na linha: " + linha);
				}
				String categoria = campos[5].trim();
				produtos.add(new Produto(nome, modelo, marca, preco, categoria));
			}
		}
		return produtos;
	}

	/**
	 Salva uma lista de produtos em um arquivo texto.
	 <p>
	 Este método pode utilizar a classe {@link BufferedWriter} ou {@link Formatter} (ou ainda outras),
	 que são eficientes para gravação de arquivos texto, e a classe {@link Files},
	 que fornece métodos utilitários para manipulação de caminhos e arquivos, além de
	 {@link Path} e {@link Paths}.
	 <p>
	 Cada produto é salvo em uma linha, com seus atributos separados por ponto e vírgula (`;`).
	 A escolha de `;` como separador evita problemas com vírgulas que podem existir nos atributos.
	 O formato de cada linha deve ser:
	 <pre>
	 PRODUTO;nome;modelo;marca;preco;nomeCategoria
	 </pre>
	 <p>
	 Exemplo de arquivo gerado:
	 <pre>
	 PRODUTO;Smartphone;Galaxy S21;Samsung;5000.0;Eletrônicos
	 PRODUTO;Notebook;XPS 13;Dell;9000.0;Informática
	 </pre>

	 @param produtos Lista de produtos a salvar no arquivo.
	 @param filePath Caminho completo do arquivo onde os produtos serão salvos.

	 @throws IOException Caso ocorra um erro ao criar ou gravar no arquivo.
	 */
	public static void salvarProdutos(List<Produto> produtos, String filePath) throws IOException {
		try (BufferedWriter writer = Files.newBufferedWriter(Paths.get(filePath))) {
			for (Produto produto : produtos) {
				// Escreve os atributos do produto separados por ponto e vírgula
				writer.write("PRODUTO" + ";"
						+ produto.getNome() + ";"
						+ produto.getModelo() + ";"
						+ produto.getMarca() + ";"
						+ produto.getPreco() + ";"
						+ produto.getNomeCategoria() + System.lineSeparator());
			}
		}
	}

	public Produto(String nome, String modelo, String marca, double preco, String nomeCategoria) {
		this.nome = nome;
		this.modelo = modelo;
		this.marca = marca;
		this.preco = preco;
		this.nomeCategoria = nomeCategoria;
		this.categoria = null;
	}

	public Produto(String nome, String modelo, String marca, double preco, Categoria categoria) {
		this.nome = nome;
		this.modelo = modelo;
		this.marca = marca;
		this.preco = preco;
		this.nomeCategoria = categoria.getNome();
		this.categoria = categoria;
	}

	@Override
	public boolean equals(Object o) {
		if (!(o instanceof Produto)) {
			return false;
		}
		Produto produto = (Produto) o;
		return Double.compare(produto.preco, preco) == 0
				&& Objects.equals(nome, produto.nome)
				&& Objects.equals(modelo, produto.modelo)
				&& Objects.equals(marca, produto.marca)
				&& Objects.equals(nomeCategoria, produto.nomeCategoria);
	}

	public Categoria getCategoria() {
		return categoria;
	}

	public String getMarca() {
		return marca;
	}

	public String getModelo() {
		return modelo;
	}

	// Getters
	public String getNome() {
		return nome;
	}

	public String getNomeCategoria() {
		return nomeCategoria;
	}

	public double getPreco() {
		return preco;
	}

	@Override
	public int hashCode() {
		return Objects.hash(nome, modelo, marca, preco, nomeCategoria);
	}

	/**
	 Converte os atributos de um produto para uma string formatada no estilo CSV
	 (valores separados por ponto e vírgula), para que possa ser salvo em um arquivo texto.

	 @return Uma string formatada contendo o nome "PRODUTO" e os valores dos atributos do produto.

	 <p>
	 Este método prepara os dados do produto para armazenamento em arquivo texto,
	 no formato:
	 <pre>
	 PRODUTO;nome;modelo;marca;preco;nomeCategoria
	 </pre>
	 Os valores individuais são separados por ponto e vírgula para permitir a leitura posterior.

	 Detalhes do funcionamento:
	 <ul>
	 <li>Os atributos do objeto são convertidos para strings individuais.</li>
	 <li>As strings podem unidas por ponto e vírgula usando o método {@link String#join}, ou manualmente.</li>
	 <li>O método retorna a string resultante, que representa o nome da classe e todos os atributos do produto.</li>
	 </ul>
	 </p>
	 */
	public String salvarProduto() {
		return "PRODUTO" + ";" + nome + ";" + modelo + ";" + marca + ";" + preco + ";" + nomeCategoria;
	}

	@Override
	public String toString() {
		return "Produto{"
				+ "nome='" + nome + '\''
				+ ", modelo='" + modelo + '\''
				+ ", marca='" + marca + '\''
				+ ", preco=" + preco
				+ ", categoria='" + nomeCategoria + '\''
				+ '}';
	}
	private Categoria categoria;
	private String marca;
	private String modelo;
	private String nome;
	private String nomeCategoria;
	private double preco;
}
