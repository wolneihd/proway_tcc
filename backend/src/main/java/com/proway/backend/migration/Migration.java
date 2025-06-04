package com.proway.backend.migration;

import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

import com.proway.backend.enums.LLM;
import com.proway.backend.models.Categoria;
import com.proway.backend.models.Configs;
import com.proway.backend.models.Feedback;
import com.proway.backend.repositories.CategoriaRepository;
import com.proway.backend.repositories.ConfigsRepository;
import com.proway.backend.repositories.FeedbackRepository;

@Configuration
@Profile("test")
public class Migration implements CommandLineRunner {

    @Autowired
    private CategoriaRepository categoriaRepository;

    @Autowired
    private FeedbackRepository feedbackRepository;

    @Autowired
    private ConfigsRepository configsRepository;

    @Override
    public void run(String... args) throws Exception {

        List<String> categorias = Arrays.asList("Limpeza", "Organização",
                "Atendimento", "Preço", "Tempo de espera", "Produto", "Ambiente", "Segurança",
                "Acessibilidade", "Outro");

        List<String> feedbacks = Arrays.asList("Positivo", "Neutro", "Negativo");


        for (String s : categorias) {
            categoriaRepository.save(new Categoria(null, s));
        }

        for (String s : feedbacks) {
            feedbackRepository.save(new Feedback(null, s));
        }

        String dummyURL = "www.powerbi.com";
        String dummyChaveLLM = "www.powerbi.com";

        configsRepository.save(new Configs(null, LLM.GROQIA, dummyURL, dummyChaveLLM));
        
    }
}
