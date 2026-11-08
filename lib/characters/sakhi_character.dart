/// The Sakhi cast: animals drawn as people, one guide per app feature.
///
/// Artwork lives in `assets/characters/` (regenerate with
/// `python3 tools/generate_characters.py`). Render with `flutter_svg`:
///
/// ```dart
/// SvgPicture.asset(SakhiCast.forFeature(SakhiFeature.sos).assetPath)
/// ```
///
/// Remember to list `assets/characters/` under `flutter: assets:` in
/// pubspec.yaml.
library;

enum SakhiFeature {
  symptomChecker,
  voiceAssistant,
  pregnancyCare,
  facilityFinder,
  nutritionScanner,
  sos,
}

class SakhiCharacter {
  const SakhiCharacter({
    required this.id,
    required this.name,
    required this.animal,
    required this.feature,
    required this.role,
    required this.personality,
    required this.catchphrase,
    required this.greetings,
    required this.colorValue,
  });

  /// Stable identifier; also the SVG file name.
  final String id;
  final String name;
  final String animal;
  final SakhiFeature feature;

  /// One line on what this character does in the app.
  final String role;
  final String personality;

  /// English line the character says when its screen opens.
  final String catchphrase;

  /// Short self-introduction keyed by language code (en, hi, kn).
  /// Add the remaining app languages through the normal l10n review.
  final Map<String, String> greetings;

  /// Signature ARGB colour, e.g. `Color(character.colorValue)`.
  final int colorValue;

  String get assetPath => 'assets/characters/$id.svg';

  String greeting(String languageCode) =>
      greetings[languageCode] ?? greetings['en']!;
}

class SakhiCast {
  SakhiCast._();

  static const drGanga = SakhiCharacter(
    id: 'dr_ganga_elephant',
    name: 'Dr. Ganga',
    animal: 'Elephant',
    feature: SakhiFeature.symptomChecker,
    role: 'Asks gentle questions about symptoms and explains what to do next.',
    personality: 'Calm, wise, never in a hurry. Remembers everything you tell her.',
    catchphrase: 'Tell me slowly, where does it hurt?',
    greetings: {
      'en': 'Namaste! I am Dr. Ganga.',
      'hi': 'नमस्ते! मैं डॉ. गंगा हूँ।',
      'kn': 'ನಮಸ್ಕಾರ! ನಾನು ಡಾ. ಗಂಗಾ.',
    },
    colorValue: 0xFF2A9D8F,
  );

  static const mira = SakhiCharacter(
    id: 'mira_mynah',
    name: 'Mira',
    animal: 'Mynah',
    feature: SakhiFeature.voiceAssistant,
    role: 'Listens and talks back, so nobody needs to read or type.',
    personality: 'Chatty, cheerful, patient. Happy to repeat things as often as needed.',
    catchphrase: 'Just speak, I am listening!',
    greetings: {
      'en': 'Namaste! I am Mira.',
      'hi': 'नमस्ते! मैं मीरा हूँ।',
      'kn': 'ನಮಸ್ಕಾರ! ನಾನು ಮೀರಾ.',
    },
    colorValue: 0xFF2E7D32,
  );

  static const champa = SakhiCharacter(
    id: 'champa_hen',
    name: 'Champa',
    animal: 'Hen',
    feature: SakhiFeature.pregnancyCare,
    role: 'Tracks pregnancy week by week and reminds about check-ups and vaccines.',
    personality: 'Warm, motherly and protective, like the village ASHA didi.',
    catchphrase: 'You and your baby are my little chicks.',
    greetings: {
      'en': 'Namaste! I am Champa.',
      'hi': 'नमस्ते! मैं चंपा हूँ।',
      'kn': 'ನಮಸ್ಕಾರ! ನಾನು ಚಂಪಾ.',
    },
    colorValue: 0xFFEC407A,
  );

  static const chiku = SakhiCharacter(
    id: 'chiku_squirrel',
    name: 'Chiku',
    animal: 'Palm squirrel',
    feature: SakhiFeature.facilityFinder,
    role: 'Finds the nearest PHC, hospital or pharmacy and shows the way.',
    personality: 'Quick, curious, knows every lane and shortcut.',
    catchphrase: 'Follow me, the clinic is close by!',
    greetings: {
      'en': 'Namaste! I am Chiku.',
      'hi': 'नमस्ते! मैं चीकू हूँ।',
      'kn': 'ನಮಸ್ಕಾರ! ನಾನು ಚೀಕು.',
    },
    colorValue: 0xFFF2B134,
  );

  static const bhoomi = SakhiCharacter(
    id: 'bhoomi_rabbit',
    name: 'Bhoomi',
    animal: 'Rabbit',
    feature: SakhiFeature.nutritionScanner,
    role: 'Looks at a plate of food and suggests local, affordable ways to eat better.',
    personality: 'Practical and encouraging. Loves greens, millets and dal.',
    catchphrase: 'Show me your thali!',
    greetings: {
      'en': 'Namaste! I am Bhoomi.',
      'hi': 'नमस्ते! मैं भूमि हूँ।',
      'kn': 'ನಮಸ್ಕಾರ! ನಾನು ಭೂಮಿ.',
    },
    colorValue: 0xFFEF6C00,
  );

  static const tara = SakhiCharacter(
    id: 'tara_tigress',
    name: 'Tara',
    animal: 'Tigress',
    feature: SakhiFeature.sos,
    role: 'Sends an emergency alert with location to family and the nearest help.',
    personality: 'Brave, steady and fast. Speaks in short, clear sentences in an emergency.',
    catchphrase: 'Do not worry, help is on the way.',
    greetings: {
      'en': 'Namaste! I am Tara.',
      'hi': 'नमस्ते! मैं तारा हूँ।',
      'kn': 'ನಮಸ್ಕಾರ! ನಾನು ತಾರಾ.',
    },
    colorValue: 0xFFD62839,
  );

  static const all = <SakhiCharacter>[drGanga, mira, champa, chiku, bhoomi, tara];

  static SakhiCharacter forFeature(SakhiFeature feature) =>
      all.firstWhere((c) => c.feature == feature);
}
