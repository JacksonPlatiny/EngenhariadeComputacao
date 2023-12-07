package Atividade1;

import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;

public class BolaTest {
    private Bola bola;

    @Before
    public void setUp() {
        // Configuração inicial antes de cada teste
        bola = new Bola("vermelha");
    }

    @Test
    public void testGetCor() {
        assertEquals("vermelha", bola.getCor());
    }

    @Test
    public void testSetCor() {
        bola.setCor("azul");
        assertEquals("azul", bola.getCor());
    }
}
