
import org.junit.*;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;


public class TenisTest {
    
    public TenisTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }
    @Test
    public void prueba1(){
        System.out.println("Prueba");
        Tenis tenis= new Tenis(1);
        Jugador j1= new Jugador("1", "0");
        Jugador j2= new Jugador("2", "0");
        
        Jugador j1prueba= new Jugador("1", "0");
        Jugador j2prueba= new Jugador("2", "0");
        
      //1
        j1=tenis.anotarPuntos(j1);
        String res= "J1="+"15"+"\n"+"J2="+"0";
        assertEquals(tenis.Puntaje(j1, j2),res);
      //2
         j2=tenis.anotarPuntos(j2);
        res= "J1="+"15"+"\n"+"J2="+"15";
        assertEquals(tenis.Puntaje(j1, j2),res);
       //3
         j1=tenis.anotarPuntos(j1);
       res= "J1="+"30"+"\n"+"J2="+"15";
        assertEquals(tenis.Puntaje(j1, j2),res);
        //4
         j1=tenis.anotarPuntos(j1);
        res= "J1="+"40"+"\n"+"J2="+"15";
        assertEquals(tenis.Puntaje(j1, j2),res);
        //5
         j2=tenis.anotarPuntos(j2);
         res= "J1="+"30"+"\n"+"J2="+"30";
        assertEquals(tenis.Puntaje(j1, j2),res);
        //6
         j1=tenis.anotarPuntos(j1);
         res= "J1="+"set"+"\n"+"J2="+"30";
        assertEquals(tenis.Puntaje(j1, j2),res);
       //7
         j1=tenis.anotarPuntos(j1);
         res= "J1="+"deuse"+"\n"+"J2="+"30\nJ1=GANADOR";
        assertEquals(tenis.Puntaje(j1, j2),res);
          //8
         j2=tenis.anotarPuntos(j2);
         res= "J1="+"deuse"+"\n"+"J2="+"40\n\nJ2=GANADOR";
        assertEquals(tenis.Puntaje(j1, j2),res);
    }

}
