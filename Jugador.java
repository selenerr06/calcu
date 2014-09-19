
public class Jugador {
   String id;
   String puntaje;
   String sets;

    public Jugador(String id, String puntaje) {
        this.id = id;
        this.puntaje = puntaje;
    }

    public String getId() {
        return id;
    }

    public String getSets() {
        return sets;
    }

    public void setSets(String sets) {
        this.sets = sets;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPuntaje() {
        return puntaje;
    }

    public void setPuntaje(String puntaje) {
        this.puntaje = puntaje;
    }
   
   
}

