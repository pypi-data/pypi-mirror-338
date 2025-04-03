#[derive(PartialEq, Eq, PartialOrd, Ord, Copy, Clone, Debug)]
pub struct LocalTime(crate::private::Time);

impl LocalTime {
    #[cfg(feature = "serde")]
    pub(crate) fn type_name() -> &'static str {
        "local time"
    }

    pub fn from_hms(hour: u8, minute: u8, second: u8) -> Self {
        Self(crate::private::Time {
            hour,
            minute,
            second,
            nanosecond: 0,
        })
    }

    pub fn from_hms_milli(hour: u8, minute: u8, second: u8, millisecond: u32) -> Self {
        Self(crate::private::Time {
            hour,
            minute,
            second,
            nanosecond: millisecond * 1_000_000,
        })
    }

    pub fn hour(&self) -> u8 {
        self.0.hour
    }

    pub fn minute(&self) -> u8 {
        self.0.minute
    }

    pub fn second(&self) -> u8 {
        self.0.second
    }

    pub fn nanosecond(&self) -> u32 {
        self.0.nanosecond
    }
}

impl std::str::FromStr for LocalTime {
    type Err = crate::parse::Error;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match crate::private::DateTime::from_str(s) {
            Ok(crate::private::DateTime {
                date: None,
                time: Some(time),
                offset: None,
            }) => Ok(Self(time)),
            Ok(_) => Err(crate::parse::Error::ExpectedLocalTime),
            Err(error) => Err(error.into()),
        }
    }
}

impl std::fmt::Display for LocalTime {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        self.0.fmt(f)
    }
}

#[cfg(feature = "serde")]
impl serde::ser::Serialize for LocalTime {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: serde::ser::Serializer,
    {
        crate::private::DateTime::from(self.0).serialize(serializer)
    }
}

#[cfg(feature = "serde")]
impl<'de> serde::de::Deserialize<'de> for LocalTime {
    fn deserialize<D>(deserializer: D) -> Result<LocalTime, D::Error>
    where
        D: serde::de::Deserializer<'de>,
    {
        match crate::private::DateTime::deserialize(deserializer)? {
            crate::private::DateTime {
                date: None,
                time: Some(time),
                offset: None,
            } => Ok(LocalTime(time)),
            datetime => Err(serde::de::Error::invalid_type(
                serde::de::Unexpected::Other(datetime.type_name()),
                &Self::type_name(),
            )),
        }
    }
}

#[cfg(feature = "chrono")]
impl From<chrono::NaiveTime> for LocalTime {
    fn from(value: chrono::NaiveTime) -> Self {
        use chrono::Timelike;

        Self(crate::private::Time {
            hour: value.hour() as u8,
            minute: value.minute() as u8,
            second: value.second() as u8,
            nanosecond: value.nanosecond() as u32,
        })
    }
}
