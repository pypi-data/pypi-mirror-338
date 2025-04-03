
def test_plugin():
    import polars as pl
    import polars.selectors as cs
    from polars_textproc import repetition_signals

    english = """
    English is a West Germanic language in the Indo-European language family, whose speakers, called Anglophones, originated in early medieval England on the island of Great Britain.[4][5][6] The namesake of the language is the Angles, one of the Germanic peoples that migrated to Britain after its Roman occupiers left. English is the most spoken language in the world, primarily due to the global influences of the former British Empire (succeeded by the Commonwealth of Nations) and the United States.[7] English is the third-most spoken native language, after Mandarin Chinese and Spanish;[8] it is also the most widely learned second language in the world, with more second-language speakers than native speakers.

    English is either the official language or one of the official languages in 59 sovereign states (such as India, Ireland, and Canada). In some other countries, it is the sole or dominant language for historical reasons without being explicitly defined by law (such as in the United States and United Kingdom).[9] It is a co-official language of the United Nations, the European Union, and many other international and regional organisations. It has also become the de facto lingua franca of diplomacy, science, technology, international trade, logistics, tourism, aviation, entertainment, and the Internet.[10] English accounts for at least 70% of total native speakers of the Germanic languages, and Ethnologue estimated that there were over 1.5 billion speakers worldwide as of 2021.[3]"""

    swedish = """
    Engelska (English) är ett västgermanskt språk, dock starkt påverkat av bland annat franska och latin. Det är världens mest spridda språk och fungerar i många delar av världen som lingua franca.[2]
    Historia

    Engelskan är ett västgermanskt språk. Det nu talade västgermanska språk som räknas som närmast besläktat med engelskan är lågskotskan (Scots) och därefter frisiskan.[3] Uppemot 7 500 ord i engelskans aktiva ordförråd är franska lånord som en följd av den normandiska invasionen av England år 1066 efter slaget vid Hastings.[4] Germanska språkvarieteter kom även tidigare till de brittiska öarna på 400-talet med olika germanska stammar. Dessa har traditionellt beskrivits som främst saxare (talande saxiska dialekter) och angler (talande angliska dialekter) som tillsammans fått beteckningen anglosaxare, samt även jutar, friser och franker.[4] Britannien hade tidigare varit bebott främst av kelter, som talade keltiska språk, men dessa trängdes undan av germanerna. De keltiska folken fortsatte länge att vara dominerande i Skottland och Wales samt på Irland. De keltiska språken återfinns även i modern tid som iriska, skotsk gaeliska och kymriska, och fanns t.o.m. år 1777 i Cornwall."""

    interlingua = """
    Le lingua anglese[1] es un lingua germanic con influentia del lingua latin, gratias al influentia del lingua francese diffundite durante le regno normanne del Anglaterra a partir de 1066.
    Stato

    Iste lingua non es parlate per le major numero del humanos in le mundo (vide lingua chinese mandarin), ma illo es inseniate in tote le mundo. Illo ha quasi devenite un lingua mundial, sovente usate como lingua franca. Il ha de 347.600.000 a 580.000.000 de parlantes in le mundo del quales circa 60.000.000 vive in Europa. Le anglese es un del linguas fontes primari de Interlingua e un del linguas official del Union Europee e del Nationes Unite. """

    repetetive = """
    This is a very repetetive text that is very repetetive and a text
    """ * 10


    df = pl.DataFrame({
        "text": [english, swedish, interlingua, None, repetetive], 
        "num" : [1, 2, 3, 4, 5],
        })

    lf = df.lazy()

    lf = lf.with_columns(repetition=repetition_signals("text"))#, langid=fasttext("text", path="model.bin", labels=["__label__swe_Latn", "__label__eng_Latn"]))
    lf = lf.unnest('repetition')#.unnest('langid')

    df = lf.collect()
    
    signals = df.select(cs.ends_with('gram_char_ratio'))
    assert (signals.max() == signals[4]).select(all=pl.all_horizontal('*')).item()
