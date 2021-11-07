import Cocoa

extension String {
    init(unicodeScalar: UnicodeScalar) {
        self.init(Character(unicodeScalar))
    }
    
    
    init?(unicodeCodepoint: Int) {
        if let unicodeScalar = UnicodeScalar(unicodeCodepoint) {
            self.init(unicodeScalar: unicodeScalar)
        } else {
            return nil
        }
    }
    
    
    static func +(lhs: String, rhs: Int) -> String {
        return lhs + String(unicodeCodepoint: rhs)!
    }
    
    
    static func +=(lhs: inout String, rhs: Int) {
        lhs = lhs + rhs
    }
}

var ints = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print(ints.compactMap { String(unicodeCodepoint:$0) }.reduce("") {$0 + $1})
