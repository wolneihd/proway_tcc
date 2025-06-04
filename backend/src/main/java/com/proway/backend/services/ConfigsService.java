package com.proway.backend.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.proway.backend.models.Configs;
import com.proway.backend.repositories.ConfigsRepository;

import jakarta.persistence.EntityNotFoundException;

@Service
public class ConfigsService {
    
    @Autowired
    private ConfigsRepository configsRepository;

    public Configs findFirst() {
        return configsRepository.findById(1L).get();        
    }

    public Configs updateConfigs(Configs configs) {
        if (configs.getLLM() == null || configs.getUrlPowerBI() == null || configs.getChaveLLM() == null) {
            throw new IllegalArgumentException("Algum dos parâmetros informados está nulo");
        }

        Configs existing = configsRepository.findById(1L)
                .orElseThrow(() -> new EntityNotFoundException("Configuração não encontrada"));

        // Atualizar os campos
        existing.setLLM(configs.getLLM());
        existing.setUrlPowerBI(configs.getUrlPowerBI());
        existing.setChaveLLM(configs.getChaveLLM());

        // Salvar e retornar
        return configsRepository.save(existing);
    }
}
