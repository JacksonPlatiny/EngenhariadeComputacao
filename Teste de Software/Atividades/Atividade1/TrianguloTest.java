package Atividade1;

import static org.junit.Assert.assertEquals;
//import static org.junit.Assert.assertFalse;
//import static org.junit.Assert.assertTrue;
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
}
