# TextCleaner

Cleans up messy text from PDF extraction.

When you're extracting text from PDFs you may run into several issues:

- Text is broken between lines, making sentencizing difficult or leading to unpredictable results
- Multiple spaces where there should just be one
- Words are often hyphenated between lines and broken with a space, which hinders semantic understanding
- Curly quotes and double-quotes which you may want to convert to "real" quotes

This Executor aims to fix that, turning a broken chunk of text into something more usable.

For example, if we enable all the options to fix the above bullet points:

### Before

```
IN  EVERY  FIELD  OF  ENDEAVOR  THERE  ARE  A  FEW  FIGURES  WHOSE  ACCOM- 
plishment  and  influence  cause  them  to  be  the  symbols  of  their  age; 
their  careers  and  oeuvres  become  the  touchstones  by  which  the 
field  is  measured  and  its  history  told.  In  the  related  pursuits  of 
analytical  and  descriptive  bibliography,  textual  criticism,  and  scholarly 
editing,  Fredson  Bowers  was  such  a  figure,  dominating  the  four  decades 
after  1949,  when  his  Principles  of  Bibliographical  Description  was  pub- 
lished.  By  1973  the  period  was  already  being  called  “the  age  of  Bowers’": 
in  that  year  Norman  Sanders,  writing  the  chapter  on  textual  scholarship 
for  Stanley  Wells's  Shakespeare:  Select  Bibliographies,  gave  this  title  to 
a  section  of  his  essay.  For  most  people,  it  would  be  achievement  enough 
to  rise  to  such  a  position  in  a  field  as  complex  as  Shakespearean  textual 
studies;  but  Bowers  played  an  equally  important  role  in  other  areas. 
Editors  of  nineteenth-century  American  authors,  for  example,  would 
also  have  to  call  the  recent  past  “the  age  of  Bowers,”  as  would  the  writers 
of  descriptive  bibliographies  of  authors  and  presses.  His  ubiquity  in 
the  broad  field  of  bibliographical  and  textual  study,  his  seemingly  com- 
plete  possession  of  it,  distinguished  him  from  his  illustrious  predeces- 
sors  and  made  him  the  personification  of  bibliographical  scholarship  in 
his  time. 
When  in  1969  Bowers  was  awarded  the  Gold  Medal  of  the  Biblio- 
graphical  Society  in  London,  John  Carter’s  citation  referred  to  the 
Principles  as  “majestic,”  called  Bowers’s  current  projects  “formidable,” 
said  that  he  had  “imposed  critical  discipline””  on  the  texts  of  several 
authors,  described  Studies  in  Bibliography  as  a  “‘great  and  continuing 
achievement,”  and  included  among  his  characteristics  “‘uncompromising 
seriousness  of  purpose”  and  “professional  intensity.”  Bowers  was  not 
unaccustomed  to  such  encomia,  but  he  had  also  experienced  his  share  of 
attacks:  his  scholarly  positions  were  not  universally  popular,  and  he 
expressed  them  with  an  aggressiveness  that  almost  seemed  calculated  to
```

### After

```
IN EVERY FIELD OF ENDEAVOR THERE ARE A FEW FIGURES WHOSE ACCOMplishment and influence cause them to be the symbols of their age; their careers and oeuvres become the touchstones by which the field is measured and its history told. In the related pursuits of analytical and descriptive bibliography, textual criticism, and scholarly editing, Fredson Bowers was such a figure, dominating the four decades after 1949, when his Principles of Bibliographical Description was published. By 1973 the period was already being called "the age of Bowers’": in that year Norman Sanders, writing the chapter on textual scholarship for Stanley Wells's Shakespeare: Select Bibliographies, gave this title to a section of his essay. For most people, it would be achievement enough to rise to such a position in a field as complex as Shakespearean textual studies; but Bowers played an equally important role in other areas. Editors of nineteenth-century American authors, for example, would also have to call the recent past "the age of Bowers," as would the writers of descriptive bibliographies of authors and presses. His ubiquity in the broad field of bibliographical and textual study, his seemingly complete possession of it, distinguished him from his illustrious predecessors and made him the personification of bibliographical scholarship in his time. When in 1969 Bowers was awarded the Gold Medal of the Bibliographical Society in London, John Carter’s citation referred to the Principles as "majestic," called Bowers’s current projects "formidable," said that he had "imposed critical discipline"" on the texts of several authors, described Studies in Bibliography as a "'great and continuing achievement," and included among his characteristics "'uncompromising seriousness of purpose" and "professional intensity." Bowers was not unaccustomed to such encomia, but he had also experienced his share of attacks: his scholarly positions were not universally popular, and he expressed them with an aggressiveness that almost seemed calculated to
```
