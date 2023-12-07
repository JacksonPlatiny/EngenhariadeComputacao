package Atividade3;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TrianguloTest {
    @Test
    public void testTrianguloEscalenoValido() {
        Triangulo triangulo = new Triangulo(3.0, 4.0, 5.0);
        assertEquals("Escaleno", triangulo.classificarTriangulo());
    }

    @Test
    public void testTrianguloIsoscelesValido() {
        Triangulo triangulo = new Triangulo(5.0, 5.0, 7.0);
        assertEquals("Isósceles", triangulo.classificarTriangulo());
    }

    @Test
    public void testTrianguloEquilateroValido() {
        Triangulo triangulo = new Triangulo(4.0, 4.0, 4.0);
        assertEquals("Equilátero", triangulo.classificarTriangulo());
    }

    @Test
    public void testLadoZero() {
        Triangulo triangulo = new Triangulo(3.0, 0.0, 5.0);
        assertEquals("Não é um triângulo", triangulo.classificarTriangulo());
    }

    @Test
    public void testLadoNegativo() {
        Triangulo triangulo = new Triangulo(-2.0, 3.0, 4.0);
        assertEquals("Não é um triângulo", triangulo.classificarTriangulo());
    }

    @Test
    public void testSomaDeDoisLadosIgualAoTerceiro() {
        Triangulo triangulo = new Triangulo(3.0, 4.0, 7.0);
        assertEquals("Não é um triângulo", triangulo.classificarTriangulo());
    }

    @Test
    public void testCalculaPerimetro() {
        Triangulo triangulo = new Triangulo(3.0, 4.0, 5.0);
        assertEquals(12.0, triangulo.calculaPerimetro(), 0.01);
    }

    @Test
    public void testCalculaArea() {
        Triangulo triangulo = new Triangulo(3.0, 4.0, 5.0);
        assertEquals(6.0, triangulo.calculaArea(), 0.01);
    }
    
    @Test
    public void testCalculaPerimetro2() {
        Triangulo triangulo2 = new Triangulo(6.0, 7.0, 8.0);
        assertEquals(21.0, triangulo2.calculaPerimetro(), 0.01);
    }

    @Test
    public void testCalculaArea2() {
        Triangulo triangulo2 = new Triangulo(6.0, 7.0, 8.0);
        assertEquals(20.33317, triangulo2.calculaArea(), 0.01);
    }
}
