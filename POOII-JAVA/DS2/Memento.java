package DS2;

import java.util.List;

public class Memento {
    private final List<Item> estado;

    public Memento(List<Item> estado) {
        this.estado = estado;
    }

    public List<Item> getEstado() {
        return estado;
    }
}
