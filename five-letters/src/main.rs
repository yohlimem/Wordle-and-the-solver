use std::fs;
use std::io::Write;


fn main() {
    let words = fs::read_to_string("adjectives.txt").expect("Unable to read file");
    let five_letter_words = words.lines().filter(|word| word.chars().count() == 5 && !word.contains('\'') && !word.contains('\"')).collect::<Vec<_>>().join("\n");

    let mut five_letter_words_file = fs::File::create("five_letter_words.txt").expect("Unable to create file");
    five_letter_words_file.write(five_letter_words.as_bytes()).expect("Unable to write data");

    let words = fs::read_to_string("nouns.txt").expect("Unable to read file");
    let five_letter_words = words.lines().filter(|word| word.chars().count() == 5 && !word.contains('\'') && !word.contains('\"')).collect::<Vec<_>>().join("\n");
    five_letter_words_file.write(five_letter_words.as_bytes()).expect("Unable to write data");

    let words = fs::read_to_string("prepositions.txt").expect("Unable to read file");
    let five_letter_words = words.lines().filter(|word| word.chars().count() == 5 && !word.contains('\'') && !word.contains('\"')).collect::<Vec<_>>().join("\n");
    five_letter_words_file.write(five_letter_words.as_bytes()).expect("Unable to write data");
}
