package com.proway.backend.models;

import java.util.Arrays;
import java.util.List;

import com.proway.backend.enums.LLM;
import com.proway.backend.enums.TipoMensagem;

public class Frontend {

    private List<LLM> llms;
    private List<TipoMensagem> tipoMensagems;

    public Frontend() {
        this.llms = Arrays.asList(LLM.CHATGPT, LLM.GEMINI, LLM.GROQIA);
        this.tipoMensagems = Arrays.asList(TipoMensagem.AUDIO, TipoMensagem.IMAGEM, TipoMensagem.TEXTO);
    }

    public List<LLM> getLlms() {
        return llms;
    }

    public List<TipoMensagem> getTipoMensagems() {
        return tipoMensagems;
    }
}
