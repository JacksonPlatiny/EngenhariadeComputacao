package Atividade1;

import static org.junit.Assert.assertEquals;
//import static org.junit.Assert.assertThrows;
import org.junit.Before;
import org.junit.Test;

public class CalculadoraTest {
    private Calculadora calculadora;

    @Before
    public void setUp() {
        // Configuração inicial antes de cada teste
        calculadora = new Calculadora();
    }

    @Test
    public void testSomar() {
        assertEquals(5, calculadora.somar(2, 3), 0.0); // Usamos 0.001 de margem de erro para comparação de números de ponto flutuante
    }

    @Test
    public void testSubtrair() {
        assertEquals(-1, calculadora.subtrair(2, 3), 0.0);
    }

    @Test
    public void testMultiplicar() {
        assertEquals(6, calculadora.multiplicar(2, 3), 0.0);
    }

    @Test
    public void testDividir() {
        assertEquals(2, calculadora.dividir(6, 3), 0.0);
    }

    @Test(expected = ArithmeticException.class)
    public void testDividirPorZero() {
        calculadora.dividir(6, 0);
    }
}
