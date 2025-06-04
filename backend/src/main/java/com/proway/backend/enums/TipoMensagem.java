package com.proway.backend.enums;

public enum TipoMensagem {

    TEXTO(1),
    AUDIO(2),
    IMAGEM(3);

    private int code;

    private TipoMensagem(int code) {
        this.code = code;
    }

    public int getCode() {
        return code;
    }
}
