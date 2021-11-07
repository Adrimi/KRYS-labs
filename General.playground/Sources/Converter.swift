import Foundation

public enum Converter {
    public static func asciiBinaryToString(_ input: Int) -> String {
        String(unicodeCodepoint: input) ?? ""
    }
}
