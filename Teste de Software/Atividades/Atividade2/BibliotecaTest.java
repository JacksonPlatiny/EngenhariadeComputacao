package Atividade2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class BibliotecaTest {

    @Test
    public void testPatrimonioHistorico_AnosMenoresQue1980() {
        Biblioteca biblioteca = new Biblioteca("Biblioteca Antiga", "1234567890", 1970);
        assertTrue(biblioteca.patrimonioHistorico());
    }

    @Test
    public void testPatrimonioHistorico_Ano1980() {
        Biblioteca biblioteca = new Biblioteca("Biblioteca da Transição", "0987654321", 1980);
        assertFalse(biblioteca.patrimonioHistorico());
    }

    @Test
    public void testPatrimonioHistorico_AnoMaiorQue1980() {
        Biblioteca biblioteca = new Biblioteca("Biblioteca Moderna", "5432109876", 1990);
        assertFalse(biblioteca.patrimonioHistorico());
    }

    @Test
    public void testGetNome() {
        Biblioteca biblioteca = new Biblioteca("Minha Biblioteca", "1122334455", 1975);
        assertEquals("Minha Biblioteca", biblioteca.getNome());
    }

    @Test
    public void testSetNome() {
        Biblioteca biblioteca = new Biblioteca("Biblioteca Antiga", "1234567890", 1970);
        biblioteca.setNome("Biblioteca Nova");
        assertEquals("Biblioteca Nova", biblioteca.getNome());
    }

    @Test
    public void testGetCNPJ() {
        Biblioteca biblioteca = new Biblioteca("Minha Biblioteca", "1122334455", 1975);
        assertEquals("1122334455", biblioteca.getCNPJ());
    }

    @Test
    public void testSetCNPJ() {
        Biblioteca biblioteca = new Biblioteca("Biblioteca", "1234567890", 1970);
        biblioteca.setCNPJ("9876543210");
        assertEquals("9876543210", biblioteca.getCNPJ());
    }
    
    @Test
    public void testGetAnoFundacao() {
        Biblioteca biblioteca = new Biblioteca("Minha Biblioteca", "1122334455", 1975);
        assertEquals(1975, biblioteca.getAnoFundacao());
    }

    @Test
    public void testSetAnoFundacao() {
        Biblioteca biblioteca = new Biblioteca("Biblioteca Antiga", "1234567890", 1970);
        biblioteca.setAnoFundacao(1500);
        assertEquals(1500, biblioteca.getAnoFundacao());
    }
}