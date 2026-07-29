# AI Pair-Programmer with Memory

🚧 Work in progress.

Sənin kodlama tərzini, adət etdiyin pattern-ləri öyrənən və sonrakı sessiyalarda tətbiq edən lokal AI köməkçi.

## İdeya

Adi AI asistentlər hər sessiyada sıfırdan başlayır — heç bir kontekst saxlamır. Bu alət fərqlidir: kod bazandakı seçimlərini (naming convention, error handling üslubu, tez-tez işlətdiyin pattern-lər) müşahidə edir, strukturlaşdırılmış yaddaşda saxlayır, və yeni sessiyalarda bu yaddaşdan istifadə edərək sənin real üslubuna uyğun təkliflər verir.

## Planlaşdırılan Arxitektura

- **Pattern extraction** — git history və kod dəyişikliklərindən LLM ilə struktur pattern çıxarır
- **Yaddaş qatı** — insan-oxuna bilən markdown/JSON fayllar (`.ai-memory/`), qara qutu deyil
- **Suggestion engine** — yığılmış pattern-lərə əsaslanaraq kod təklifləri verir
- **Decay mexanizmi** — köhnə, artıq işlədilməyən pattern-lərin əhəmiyyəti zamanla azalır

## Tech Stack

- Python, CLI
- OpenAI (pattern extraction üçün)
- Fayl əsaslı yaddaş (markdown/JSON)

## Status

Hazırda pattern extraction qatı qurulur. Real istifadə nümunələri və eval nəticələri layihə irəlilədikcə əlavə olunacaq.

## License

MIT