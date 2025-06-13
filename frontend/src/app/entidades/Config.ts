export interface Config {
    llm: LLM[],
    powerBI: string
}

export interface LLM {
    id: number,
    nome: string,
    api_key: string,
    ia_selecionada: boolean | null
}