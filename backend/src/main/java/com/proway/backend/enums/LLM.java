package com.proway.backend.enums;

public enum LLM {
    
    GROQIA(1),
    GEMINI(2),
    CHATGPT(3);

    private int code;

    private LLM(int code) {
        this.code = code;
    }

    public int getCode() {
        return code;
    }
}
