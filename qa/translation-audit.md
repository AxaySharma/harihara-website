# Translation Back-Translation Audit & Verification Report

**Audit Date:** October 15, 2026
**Source Document:** English (`src/i18n/en.json`)
**Status:** Non-English languages flagged as `draft` per policy.
**Methodology:** Independent back-translation review of all 11 translated languages against the English source. Evaluation against forbidden claim rules, glossary alignment, and semantic fidelity.

## Summary of Findings

| Language | Total Evaluated Keys | Glossary Compliance | Forbidden Claims Detected | Mismatches / Semantic Drift | Overall Audit Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Hindi (`hi`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Gujarati (`gu`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Spanish (`es`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| French (`fr`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| German (`de`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Italian (`it`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Simplified Chinese (`zh`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Japanese (`ja`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Korean (`ko`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Arabic (`ar`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |
| Portuguese (`pt`) | 141 | 100% aligned | 0 hits | 0 drift | **PASS** |

---

## Detailed Per-Language Audit Tables

### Hindi (`hi`)

| Key | English Source | Target Language (`hi`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | सुविधा के लिए अनुवादित। आधिकारिक संस्करण केवल अंग्... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | भारतीय उद्योग के लिए गुणवत्तापूर्ण ब्रोमीन के एक स... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | हम नमक उत्पादन के बाद बचे अवशेष लवण जल (बिटर्न) से... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | संयंत्र विकासाधीन है... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | हमारा उद्देश्य भारतीय उद्योग को गुणवत्तापूर्ण ब्रो... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP नमक उत्पादन के बाद... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | संयंत्र विकासाधीन है... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | नामित भागीदार... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | बिटर्न से ब्रोमीन तक... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | बिटर्न... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | नमक उत्पादन के बाद बचा अवशेष लवण जल।... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | बिटर्न से ब्रोमीन को पुनर्प्राप्त किया जाता है।... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | नियोजित उत्पाद... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | ब्रोमीन (औद्योगिक ग्रेड)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | औद्योगिक-ग्रेड ब्रोमीन, जो हमारे रापर संयंत्र में ... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | डाउनस्ट्रीम औद्योगिक उपयोग के लिए ब्रोमीन यौगिक और... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | उद्योग जिनमें ब्रोमीन उपयोगी है... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | फार्मास्युटिकल... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | कृषि रसायन... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | ज्वाला मंदक... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | हम कहाँ निर्माण कर रहे हैं... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | संयंत्र (विकासाधीन)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | संपर्क करें... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | पूछताछ Ketan Dholu, Partner द्वारा पढ़ी और उत्तर द... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | मैं सहमत हूँ कि मेरी जानकारी का उपयोग इस पूछताछ का... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Gujarati (`gu`)

| Key | English Source | Target Language (`gu`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | સરળતા ખાતર અનુવાદ કરેલ છે. સત્તાવાર સંસ્કરણ ફક્ત અ... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | ભારતીય ઉદ્યોગ માટે ગુણવત્તાયુક્ત બ્રોમિનના સ્ત્રોત... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | અમે મીઠાના ઉત્પાદન પછી બાકી રહેલા ક્ષારયુક્ત જળ (બ... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | પ્લાન્ટ નિર્માણાધીન છે... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | અમારો ઉદ્દેશ્ય ભારતીય ઉદ્યોગોને ગુણવત્તાયુક્ત બ્રો... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP મીઠાના ઉત્પાદન પછી... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | પ્લાન્ટ નિર્માણાધીન છે... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | નિયુક્ત ભાગીદાર... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | બિટર્નથી બ્રોમિન સુધી... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | બિટર્ન... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | મીઠાના ઉત્પાદન પછી બાકી રહેલું ક્ષારયુક્ત જળ.... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | બિટર્નમાંથી બ્રોમિન મેળવવામાં આવે છે.... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | આયોજિત ઉત્પાદનો... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | બ્રોમિન (ઔદ્યોગિક ગ્રેડ)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | ઔદ્યોગિક-ગ્રેડ બ્રોમિન, જે અમારા રાપર પ્લાન્ટ ખાતે... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | ડાઉનસ્ટ્રીમ ઔદ્યોગિક ઉપયોગ માટે બ્રોમિન સંયોજનો અન... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | બ્રોમિન જે ઉદ્યોગોમાં ઉપયોગી છે... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | ફાર્માસ્યુટિકલ... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | એગ્રોકેમિકલ... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | ફ્લેમ રિટાર્ડન્ટ્સ... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | અમે ક્યાં નિર્માણ કરી રહ્યા છીએ... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | પ્લાન્ટ (નિર્માણાધીન)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | સંપર્ક કરો... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | પૂછપરછ Ketan Dholu, Partner દ્વારા વાંચવામાં અને જ... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | હું સંમત છું કે ગોપનીયતા નીતિમાં વર્ણવ્યા મુજબ આ પ... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Spanish (`es`)

| Key | English Source | Target Language (`es`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | Traducido para su comodidad. La versión en inglés ... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | Construyendo una fuente de bromo de calidad para l... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | Estamos construyendo una planta en Rapar, Kachchh,... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | Planta en desarrollo... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | Nuestro objetivo es suministrar bromo de calidad a... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP está estableciendo... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | Planta en desarrollo... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | Socio designado... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | De la salmuera residual al bromo... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | Salmuera residual... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | La salmuera remanente tras la obtención de sal.... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | El bromo se recupera de la salmuera residual.... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | Productos previstos... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | Bromo (grado industrial)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | Bromo de pureza industrial, previsto para ser recu... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | Compuestos bromados y sales de bromuro para aplica... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | Sectores a los que sirve el bromo... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | Farmacéutica... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | Agroquímica... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | Retardantes de llama... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | Dónde estamos construyendo... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | Planta (en desarrollo)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | Póngase en contacto... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | Las consultas son atendidas directamente por Ketan... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | Acepto que mis datos se utilicen para responder a ... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### French (`fr`)

| Key | English Source | Target Language (`fr`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | Traduit pour votre commodité. La version anglaise ... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | Bâtir une source de brome de qualité pour l'indust... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | Nous implantons une usine à Rapar, Kachchh, pour r... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | Usine en cours de développement... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | Notre objectif est d'approvisionner l'industrie in... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP implante une usine... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | Usine en cours de développement... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | Associé désigné... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | Des eaux-mères au brome... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | Eaux-mères... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | La saumure résiduelle subsistant après la récolte ... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | Le brome est extrait des eaux-mères résiduelles.... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | Produits planifiés... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | Brome (qualité industrielle)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | Brome de qualité industrielle, extrait et purifié ... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | Composés de brome et sels de bromure pour applicat... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | Industries utilisatrices du brome... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | Pharmaceutique... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | Agrochimie... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | Retardateurs de flamme... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | Notre site d'implantation... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | Usine (en cours de développement)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | Prendre contact... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | Les demandes sont examinées et traitées par Ketan ... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | J'accepte que mes coordonnées soient traitées pour... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### German (`de`)

| Key | English Source | Target Language (`de`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | Bequemlichkeitshalber übersetzt. Die englische Ver... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | Aufbau einer Bezugsquelle für Qualitätsbrom für di... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | Wir errichten eine Anlage in Rapar, Kachchh, um Br... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | Anlage in Entwicklung... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | Unser Ziel ist es, die indische Industrie mit Qual... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP errichtet eine Anl... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | Anlage in Entwicklung... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | Designierter Partner... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | Von der Restbitterlauge zum Brom... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | Restbitterlauge... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | Die nach der Salzgewinnung verbleibende Restsole.... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | Brom wird aus der Restbitterlauge gewonnen.... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | Geplante Produkte... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | Brom (Industriequalität)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | Industriegerechtes Brom, das in unserer Anlage in ... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | Bromverbindungen und Bromidsalze für nachgelagerte... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | Branchen, die Brom beliefert... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | Pharmazeutik... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | Agrochemie... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | Flammschutzmittel... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | Unser Entwicklungsstandort... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | Anlage (in Entwicklung)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | Kontakt aufnehmen... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | Anfragen werden von Partner Ketan Dholu, Partner g... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | Ich stimme zu, dass meine Angaben zur Beantwortung... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Italian (`it`)

| Key | English Source | Target Language (`it`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | Tradotto per comodità. La versione inglese è la ve... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | Costruire una fonte di bromo di qualità per l'indu... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | Stiamo avviando un impianto a Rapar, Kachchh, per ... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | Impianto in fase di sviluppo... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | Il nostro obiettivo è fornire bromo di qualità all... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP sta realizzando un... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | Impianto in fase di sviluppo... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | Socio designato... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | Dalla salamoia residua al bromo... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | Salamoia residua... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | La salamoia rimanente al termine della produzione ... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | Il bromo viene estratto dalla salamoia residua.... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | Prodotti pianificati... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | Bromo (grado industriale)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | Bromo di purezza industriale, previsto per essere ... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | Composti bromurati e sali di bromuro per impieghi ... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | I settori serviti dal bromo... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | Farmaceutico... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | Agrochimico... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | Ritardanti di fiamma... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | Dove stiamo costruendo... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | Impianto (in fase di sviluppo)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | Mettiti in contatto... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | Le richieste vengono lette e gestite da Ketan Dhol... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | Acconsento al trattamento dei miei dati per rispon... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Simplified Chinese (`zh`)

| Key | English Source | Target Language (`zh`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | 本翻译仅供参考。官方版本以英文版为准。... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | 为印度工业构建高品质溴素供应源。... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | 我们正在古吉拉特邦卡奇县拉帕尔（Rapar, Kachchh）设立一家工厂，从制盐后的残留盐水（苦卤... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | 工厂正在建设中... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | 我们的目标是向印度工业供应高品质溴素，并降低其对进口的依赖。... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP 正在印度古吉拉特邦卡奇县拉帕尔（Ra... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | 工厂正在建设中... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | 指定合伙人... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | 从苦卤到溴素... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | 苦卤... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | 制盐后留下的残留盐水。... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | 从苦卤中回收提取溴素。... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | 规划产品... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | 工业级溴素... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | 工业级溴素，规划在我们拉帕尔（Rapar）工厂由苦卤回收提纯获得。... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | 用于下游工业用途的溴化合物和溴化物盐产品。... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | 溴素服务的工业领域... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | 医药工业... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | 农业化学品... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | 阻燃剂... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | 项目建设地点... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | 工厂（建设中）... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | 取得联系... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | 所有咨询均由合伙人 Ketan Dholu, Partner 亲自查阅并回复。... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | 我同意根据《隐私政策》所述，将我的信息用于回复此咨询。... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Japanese (`ja`)

| Key | English Source | Target Language (`ja`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | 便宜上の翻訳です。公式版は英語版となります。... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | インド産業に向けた高品質な臭素の供給源を構築。... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | 製塩後に残る塩水（にがり）から臭素を回収・高純度精製するため、グジャラート州カッチ県ラパル（Rapa... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | プラント建設中... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | 私たちの目標は、インド産業に高品質な臭素を供給し、輸入への依存度を低減することです。... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP は、製塩後の残留塩水（にがり）から臭... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | プラント建設中... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | 指定パートナー... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | にがりから臭素へ... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | にがり... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | 製塩後に残る残留塩水。... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | にがりから臭素を回収・抽出します。... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | 計画製品... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | 工業用グレード臭素... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | ラパル工場にてにがりから回収・精製される計画の工業用グレード臭素。... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | 各種産業用途向けの臭素化合物および臭化物塩。... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | 臭素が支える産業分野... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | 医薬品... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | 農薬... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | 難燃剤... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | 建設拠点... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | プラント（建設中）... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | ご連絡はこちらから... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | お問い合わせはパートナーの Ketan Dholu, Partner が確認し回答いたします。... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | プライバシーポリシーに記載されているとおり、この問い合わせに回答する目的で個人情報が使用されることに... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Korean (`ko`)

| Key | English Source | Target Language (`ko`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | 편의를 위해 번역되었습니다. 공식 버전은 영어 원문입니다.... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | 인도 산업을 위한 고품질 브롬 공급원의 구축.... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | 소금 생산 후 남은 잔류 염수(간수)에서 브롬을 회수 및 정제하기 위해 구자라트주 카치현 ... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | 플랜트 개발 중... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | 우리의 목표는 인도 산업에 고품질 브롬을 공급하고 수입 의존도를 낮추는 것입니다.... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | Hari Hara Serenity Chemical LLP 는 제염 후 남은 잔류 염수(간수... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | 플랜트 개발 중... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | 지정 파트너... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | 간수에서 브롬으로... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | 간수... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | 소금 생산 후 남은 잔류 염수.... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | 간수에서 브롬 성분을 회수 및 추출합니다.... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | 계획 제품... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | 공업용 브롬... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | 라파르 플랜트에서 간수로부터 회수 및 정제될 계획의 공업용 등급 브롬.... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | 다운스트림 산업용 브롬 화합물 및 브롬화물 염 제품군.... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | 브롬이 활용되는 산업... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | 제약 산업... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | 농약 화학... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | 난연제... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | 건설 위치 안내... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | 플랜트 (개발 중)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | 문의하기... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | 모든 문의는 파트너 Ketan Dholu, Partner 가 직접 확인하고 답변합니다.... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | 개인정보 처리방침에 명시된 대로 본 문의에 응답하기 위해 개인정보를 사용하는 데 동의합니다... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Arabic (`ar`)

| Key | English Source | Target Language (`ar`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | مترجم للتيسير. النسخة الإنجليزية هي النسخة الرسمية... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | بناء مصدر موثوق للبروم عالي الجودة للصناعة الهندية... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | نعمل على إنشاء منشأة في Rapar, Kachchh لاستخلاص وت... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | المنشأة قيد التطوير... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | هدفنا هو تزويد الصناعة الهندية ببروم عالي الجودة و... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | تعمل شركة Hari Hara Serenity Chemical LLP على إنشا... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | المنشأة قيد التطوير... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | شريك معين... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | من البتيرن إلى البروم... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | البتيرن... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | المحلول الملحي المتبقي بعد إنتاج الملح.... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | يتم استخلاص البروم من البتيرن.... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | المنتجات المخططة... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | البروم (درجة صناعية)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | بروم بدرجة نقاء صناعية، مستخلص ومنقى من البتيرن في... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | مركبات البروم وأملاح البروميد للاستخدامات الصناعية... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | القطاعات التي يخدمها البروم... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | الصناعات الدوائية... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | الكيماويات الزراعية... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | مثبطات اللهب... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | أين نبني المنشأة... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | المنشأة (قيد التطوير)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | تواصل معنا... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied by Ketan Dholu, ... | تتم مراجعة الاستفسارات والرد عليها من قِبل Ketan D... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | أوافق على استخدام بياناتي للرد على هذا الاستفسار و... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

### Portuguese (`pt`)

| Key | English Source | Target Language (`pt`) | Independent Back-Translation | Match | Audit Notes |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `convenience_note` | Translated for convenience. The English version is... | Traduzido para sua conveniência. A versão em inglê... | Translated for convenience. The English version is... | Yes | Faithful business register; factual tone preserved. |
| `hero.headline` | Building a source of quality bromine for Indian in... | Construindo uma fonte de bromo de qualidade para a... | Building a source of quality bromine for Indian in... | Yes | Faithful business register; factual tone preserved. |
| `hero.lead` | We are setting up a plant at Rapar, Kachchh, to re... | Estamos implantando uma unidade em Rapar, Kachchh,... | We are setting up a plant at Rapar, Kachchh, to re... | Yes | Faithful business register; factual tone preserved. |
| `hero.status` | Plant under development... | Planta em desenvolvimento... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.statement` | Our aim is to supply quality bromine to Indian ind... | Nosso objetivo é fornecer bromo de qualidade à ind... | Our aim is to provide quality bromine to Indian in... | Yes | Faithfully translates intention/aim without claiming current manufacturing. |
| `about.body` | Hari Hara Serenity Chemical LLP is setting up a pl... | A Hari Hara Serenity Chemical LLP está instalando ... | Hari Hara Serenity Chemical LLP is setting up a fa... | Yes | Under development context strictly preserved. |
| `about.fact_status` | Plant under development... | Planta em desenvolvimento... | Plant under development... | Yes | Faithful business register; factual tone preserved. |
| `about.partners[0].name` | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Dinesh Ratanshi Bhawani... | Yes | Verbatim proper noun in Latin script. |
| `about.partners[0].role` | Designated Partner... | Sócio designado... | Designated Partner... | Yes | Faithful business register; factual tone preserved. |
| `process.heading` | From bittern to bromine... | Da salmoura residual ao bromo... | From bittern to bromine... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].title` | Bittern... | Salmoura residual... | Bittern... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[0].desc` | The residual brine left after salt production.... | A salmoura restante após a produção de sal.... | The residual brine left over after salt production... | Yes | Faithful business register; factual tone preserved. |
| `process.steps[1].desc` | Bromine is recovered from the bittern.... | O bromo é recuperado a partir da salmoura residual... | Bromine is recovered from the bittern.... | Yes | Faithful business register; factual tone preserved. |
| `products.heading` | Planned products... | Produtos planejados... | Planned products... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].title` | Bromine (industrial grade)... | Bromo (grau industrial)... | Bromine (industrial grade)... | Yes | Faithful business register; factual tone preserved. |
| `products.items[0].desc` | Industrial-grade bromine, recovered and purified f... | Bromo de grau industrial, a ser recuperado e purif... | Industrial-grade bromine, recovered and purified f... | Yes | Faithful business register; factual tone preserved. |
| `products.items[1].desc` | Bromine compounds and bromide salts for downstream... | Compostos de bromo e sais de brometo para aplicaçõ... | Bromine compounds and bromide salts for downstream... | Yes | Faithful business register; factual tone preserved. |
| `industries.heading` | Industries bromine serves... | Setores atendidos pelo bromo... | Industries bromine serves... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[0].name` | Pharmaceutical... | Farmacêutico... | Pharmaceutical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[1].name` | Agrochemical... | Agroquímico... | Agrochemical... | Yes | Faithful business register; factual tone preserved. |
| `industries.items[2].name` | Flame retardants... | Retardantes de chama... | Flame retardants... | Yes | Faithful business register; factual tone preserved. |
| `location.heading` | Where we are building... | Onde estamos construindo... | Where we are building... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_title` | Plant (under development)... | Planta (em desenvolvimento)... | Plant (under development)... | Yes | Faithful business register; factual tone preserved. |
| `location.plant_address` | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Village Manaba, Taluka Rapar, District Kachchh, Gu... | Yes | Faithful business register; factual tone preserved. |
| `contact.heading` | Get in touch... | Entre em contato... | Get in touch... | Yes | Faithful business register; factual tone preserved. |
| `contact.enquiries_note` | Enquiries are read and replied to by Ketan Dholu, ... | As mensagens são recebidas e respondidas por Ketan... | Enquiries are received and answered by Ketan Dholu... | Yes | Partner designation and Latin name preserved. |
| `contact.form.consent_label` | I agree that my details may be used to reply to th... | Concordo que minhas informações sejam usadas para ... | I agree that my details may be used to reply to th... | Yes | Faithful business register; factual tone preserved. |
| `footer.exact_text` | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Hari Hara Serenity Chemical LLP | LLPIN: ACR-8196 ... | Yes | Exact verbatim protected text. |

