package com.proway.backend.models;

import com.proway.backend.enums.LLM;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "configs")
public class Configs {
    
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Autoincrementado
    private Long id;

    // chaves/valores das configurações:
    private LLM llm;
    private String urlPowerBI;
    private String chaveLLM;

    public Configs() { }

    public Configs(Long id, LLM llm, String urlPowerBI, String chaveLLM) {
        this.id = id;
        this.llm = llm;
        this.urlPowerBI = urlPowerBI;
        this.chaveLLM = chaveLLM;
    }
    public static long getSerialversionuid() {
        return serialVersionUID;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public LLM getLLM() {
        return llm;
    }

    public void setLLM(LLM llm) {
        this.llm = llm;
    }
    
    public String getUrlPowerBI() {
        return urlPowerBI;
    }

    public void setUrlPowerBI(String urlPowerBI) {
        this.urlPowerBI = urlPowerBI;
    }

    public String getChaveLLM() {
        return chaveLLM;
    }

    public void setChaveLLM(String chaveLLM) {
        this.chaveLLM = chaveLLM;
    }  

}
