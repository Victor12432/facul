import java.util.ArrayList;
import java.util.List;

public class Carrinho {
    private List<Item> itens = new ArrayList<>();
    private CareTaker careTaker = new CareTaker();

    public void adicionarItem(Item item) {
        itens.add(item);
        salvarEstado(); // Salva o estado atual após a adição do item
    }

    public void removerItem(Item item) {
        itens.remove(item);
        salvarEstado(); // Salva o estado atual após a remoção do item
    }

    public double calcularTotal() {
        return itens.stream().mapToDouble(Item::getPreco).sum();
    }

    // Salva o estado atual do carrinho no CareTaker
    private void salvarEstado() {
        careTaker.salvarEstado(new Memento(new ArrayList<>(itens)));
    }

    // Desfaz a última ação realizada no carrinho
    public void desfazer() {
        Memento memento = careTaker.desfazer();
        if (memento != null) {
            this.itens = memento.getEstado();
        } else {
            System.out.println("Nenhum estado anterior para desfazer.");
        }
    }

    // Refaz a última ação desfeita no carrinho
    public void refazer() {
        Memento memento = careTaker.refazer();
        if (memento != null) {
            this.itens = memento.getEstado();
        } else {
            System.out.println("Nenhum estado posterior para refazer.");
        }
    }

    public List<Item> getItens() {
        return itens;
    }
}
