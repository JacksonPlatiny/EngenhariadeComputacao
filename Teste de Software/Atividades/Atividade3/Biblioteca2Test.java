package Atividade3;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.List;

public class Biblioteca2Test {

    @Test
    public void testAcervoPremium_ComMenosDe5Lancamentos() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Minha Biblioteca", "1122334455", 1975);

        biblioteca2.incluirLivro(new Livro("Livro 1", 2023, "Autor 1", "ISBN1"));
        biblioteca2.incluirLivro(new Livro("Livro 2", 2023, "Autor 2", "ISBN2"));
        biblioteca2.incluirLivro(new Livro("Livro 3", 2023, "Autor 3", "ISBN3"));
        biblioteca2.incluirLivro(new Livro("Livro 4", 2021, "Autor 4", "ISBN4"));

        assertFalse(biblioteca2.acervoPremium());
    }

    @Test
    public void testAcervoPremium_ComPeloMenos5Lancamentos() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Minha Biblioteca", "1122334455", 1975);

        List<Livro> livros = new ArrayList<>();
        livros.add(new Livro("Livro 1", 2023, "Autor 1", "ISBN1"));
        livros.add(new Livro("Livro 2", 2023, "Autor 2", "ISBN2"));
        livros.add(new Livro("Livro 3", 2023, "Autor 3", "ISBN3"));
        livros.add(new Livro("Livro 4", 2023, "Autor 4", "ISBN4"));
        livros.add(new Livro("Livro 5", 2023, "Autor 5", "ISBN5"));

        biblioteca2.setListaLivros(livros);

        assertTrue(biblioteca2.acervoPremium());
    }
    
    @Test
    public void testAcervoPremium_ComMenosDe5Lancamentos_SetseGets() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Minha Biblioteca", "1122334455", 1975);

        List<Livro> livros = new ArrayList<>();
        livros.add(new Livro("Livro 1", 2023, "Autor 1", "ISBN1"));
        livros.add(new Livro("Livro 2", 2023, "Autor 2", "ISBN2"));
        livros.add(new Livro("Livro 3", 2023, "Autor 3", "ISBN3"));
        livros.add(new Livro("Livro 4", 2021, "Autor 4", "ISBN4"));

        biblioteca2.setListaLivros(livros);

        assertFalse(biblioteca2.acervoPremium());
    }

    @Test
    public void testAcervoPremium_ComPeloMenos5Lancamentos_SetseGets() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Minha Biblioteca", "1122334455", 1975);

        List<Livro> livros = new ArrayList<>();
        livros.add(new Livro("Livro 1", 2023, "Autor 1", "ISBN1"));
        livros.add(new Livro("Livro 2", 2023, "Autor 2", "ISBN2"));
        livros.add(new Livro("Livro 3", 2023, "Autor 3", "ISBN3"));
        livros.add(new Livro("Livro 4", 2023, "Autor 4", "ISBN4"));
        livros.add(new Livro("Livro 5", 2023, "Autor 5", "ISBN5"));

        biblioteca2.setListaLivros(livros);
        biblioteca2.incluirLivro(new Livro("Livro 6", 2023, "Autor 6", "ISBN6"));

        assertTrue(biblioteca2.acervoPremium());
    }
    
    @Test
    public void testPatrimonioHistorico_AnosMenoresQue1980() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Biblioteca Antiga", "1234567890", 1940);
        assertTrue(biblioteca2.patrimonioHistorico());
    }

    @Test
    public void testPatrimonioHistorico_Ano1980() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Biblioteca da Transição", "0987654321", 1980);
        assertFalse(biblioteca2.patrimonioHistorico());
    }

    @Test
    public void testPatrimonioHistorico_AnoMaiorQue1980() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Biblioteca Moderna", "5432109876", 1990);
        assertFalse(biblioteca2.patrimonioHistorico());
    }

    @Test
    public void testGetNome() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Minha Biblioteca", "1122334455", 1975);
        assertEquals("Minha Biblioteca", biblioteca2.getNome());
    }

    @Test
    public void testSetNome() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Biblioteca Antiga", "1234567890", 1970);
        biblioteca2.setNome("Biblioteca Nova");
        assertEquals("Biblioteca Nova", biblioteca2.getNome());
    }

    @Test
    public void testGetCNPJ() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Minha Biblioteca", "1122334455", 1975);
        assertEquals("1122334455", biblioteca2.getCNPJ());
    }

    @Test
    public void testSetCNPJ() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Biblioteca", "1234567890", 1970);
        biblioteca2.setCNPJ("9876543210");
        assertEquals("9876543210", biblioteca2.getCNPJ());
    }
    
    @Test
    public void testGetAnoFundacao() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Minha Biblioteca", "1122334455", 1975);
        assertEquals(1975, biblioteca2.getAnoFundacao());
    }

    @Test
    public void testSetAnoFundacao() {
        Biblioteca2 biblioteca2 = new Biblioteca2("Biblioteca Antiga", "1234567890", 1970);
        biblioteca2.setAnoFundacao(1500);
        assertEquals(1500, biblioteca2.getAnoFundacao());
    }

}
