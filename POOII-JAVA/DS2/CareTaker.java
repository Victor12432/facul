package DS2;
import java.util.Stack;

public class CareTaker {
    private Stack<Memento> historicoDesfazer = new Stack<>();
    private Stack<Memento> historicoRefazer = new Stack<>();

    // Desfazendo uma ação: move o último estado para a pilha de refazer e retorna o memento removido.
    public Memento desfazer() {
        if (historicoDesfazer.isEmpty()) {
            return null;
        }
        Memento memento = historicoDesfazer.pop();
        historicoRefazer.push(memento);
        return memento;
    }

    // Refazendo uma ação: move o último estado da pilha de refazer para a pilha de desfazer e retorna o memento.
    public Memento refazer() {
        if (historicoRefazer.isEmpty()) {
            return null;
        }
        Memento memento = historicoRefazer.pop();
        historicoDesfazer.push(memento);
        return memento;
    }

    // Método para salvar um novo estado, adicionando-o ao histórico de desfazer e limpando a pilha de refazer.
    public void salvarEstado(Memento memento) {
        historicoDesfazer.push(memento);
        historicoRefazer.clear(); // Limpa a pilha de refazer, pois um novo estado foi salvo.
    }
}
