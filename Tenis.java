
public class Tenis {

    public static void main(String[] args) {
        Jugador j1= new Jugador("1", "0");
        Jugador j2= new Jugador("2", "0");
        Tenis tenis=new Tenis(1);
    }
    int tipo=0;
    Tenis(int i){
        if(i==1){
            tipo=3;
        }else{
            tipo=5;
        }
    }
    
    public Jugador anotarPuntos(Jugador jugador) {
        String puntaje = jugador.getPuntaje();
        boolean entrar = false;
        String sets=jugador.getSets();
        boolean entrar2=false;
        try{
            
        
        if( tipo>Integer.parseInt(sets)){
            
        try {
            puntaje = "" + (Integer.parseInt(puntaje));
        } catch (Exception e) {
            if (puntaje.equals("set")) {
                puntaje = "deuse";
            } else if (puntaje.equals("deuse")) {
                puntaje = "adv";
            } else if (puntaje.equals("adv")) {
                puntaje = "G A N A D O";
                sets = "" + (Integer.parseInt(sets)+1);
            }
            entrar = true;
        }
        if (!entrar) {
            if (puntaje.equals("0")) {
                puntaje = "" + (Integer.parseInt(puntaje) + 15);
            } else if (puntaje.equals("15")) {
                puntaje = "" + (Integer.parseInt(puntaje) + 15);
            } else if (puntaje.equals("30")) {
                puntaje = "" + (Integer.parseInt(puntaje) + 10);
            } else if (puntaje.equals("40")) {
                puntaje = "set";
            }
        }
        }
        }
        catch(Exception e){
            
        }
        jugador.setPuntaje(puntaje);
        return jugador;
    }
    

    public String  Puntaje(Jugador j1, Jugador j2){
        String res="";
        int sets1=0;
        int sets2=0;
        try{    
            sets1= (Integer.parseInt(j1.getSets()));
         sets2= (Integer.parseInt(j2.getSets()));
        }
      catch (Exception e){
          
      }
        
        if (j1.getId().equals("1")){
            res= "J1="+j1.getPuntaje()+"\n";
            res+="J2="+j2.getPuntaje();
            if(sets1+2==sets2){
                res+="\nJ2=GANADOR";
            }else if(sets1==sets2+2){
                 res+="\nJ1=GANADOR";
            }
        }else if (j1.getId().equals("2")) {
            res= "J1="+j2.getPuntaje()+"\n";
            res+="J2="+j1.getPuntaje();  
            if(sets1+2==sets2){
                res+="\nJ1=GANADOR";
            }else if(sets1==sets2+2){
                 res+="\nJ2=GANADOR";
            }
        }
        return res;
    } 
}
